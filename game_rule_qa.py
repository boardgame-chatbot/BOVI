# bang_rule_qa.py

import faiss
import json
import numpy as np
import os
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from memory_setup import get_memory

# ============================
# 1. 뱅 데이터/임베딩/LLM 준비
# ============================
BANG_DESC_PATH = "data/bang_description.json"     # 뱅 전체 룰 설명
BANG_FAISS_PATH = "data/bang.faiss"              # 뱅 룰/카드 청크 벡터DB
BANG_CHUNKS_PATH = "data/bang_chunks.json"       # 뱅 룰/카드 청크 텍스트

# 룰 전체 설명 로딩
with open(BANG_DESC_PATH, "r", encoding="utf-8") as f:
    bang_desc = json.load(f)["description"]   # {"description": "...룰 전체..."}

# 벡터/청크 로드
index = faiss.read_index(BANG_FAISS_PATH)
with open(BANG_CHUNKS_PATH, "r", encoding="utf-8") as f:
    chunks = json.load(f)

embed_model = SentenceTransformer("BAAI/bge-m3", device="cuda")

MODEL_NAME = "kakaocorp/kanana-1.5-2.1b-instruct-2505"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto", torch_dtype="auto")
llm_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=512)

memory = get_memory()

# ============================
# 2. 뱅 룰 요약 함수 (한번만)
# ============================
def summarize_bang_rule():
    prompt = (
        "너는 뱅(BANG!) 보드게임 룰 전문 AI야. 아래의 전체 룰을 구조적으로, 핵심 개념/목표/진행 방식/승리 조건 위주로 아주 명확하게 요약해줘. 너무 길지 않게, 초심자도 이해할 수 있게 설명해.\n\n"
        f"룰 전체:\n{bang_desc}\n\n뱅 게임의 룰을 요약해줘."
    )
    summary = llm_pipeline(prompt)[0]['generated_text']
    return summary.strip()

# ============================
# 3. 뱅 룰 Q&A 함수 (반복 호출)
# ============================
def bang_rule_qa(user_question):
    # 임베딩 + 유사도 검색
    q_vec = embed_model.encode([user_question], normalize_embeddings=True)
    _, I = index.search(np.array(q_vec), k=3)
    retrieved_chunks = [chunks[i] for i in I[0]]
    context = "\n\n".join(retrieved_chunks)

    # 메모리/대화 이력
    chat_history = memory.load_memory_variables({}).get("chat_history", [])
    chat_history_str = ""
    if chat_history:
        for turn in chat_history:
            chat_history_str += f"User: {turn['content']}\n"

    prompt = (
        "너는 뱅(BANG!) 보드게임 룰 전문 AI야. 반드시 아래 규칙을 따라야 해:\n"
        "- 답변은 반드시 아래 룰 설명(context) 범위 내에서만 생성해.\n"
        "- 룰에 없는 내용은 추측/지어내기 없이 '해당 정보는 룰에 명시되어 있지 않습니다.'라고만 답해.\n"
        "- 대화 이력, 문맥을 참고해 일관성 있게 답변해.\n"
        f"\n대화 이력:\n{chat_history_str}"
        f"\n룰 설명(context):\n{context}\n\n질문: {user_question}\n답변:"
    )
    answer = llm_pipeline(prompt)[0]['generated_text']
    memory.save_context({"input": user_question}, {"output": answer})
    return answer.strip()

# ============================
# 4. CLI 테스트용 인터페이스
# ============================
def run_bang_cli():
    print("\n🧠 뱅 게임 룰 요약 설명 (한 번만):\n")
    print(summarize_bang_rule())

    while True:
        user_q = input("\n❓ 뱅 룰/카드/역할 등에 대해 궁금한 점을 질문하세요 (종료: q): ").strip()
        if user_q.lower() == "q":
            print("종료합니다.")
            break
        answer = bang_rule_qa(user_q)
        print(f"\n💬 답변:\n{answer}")

# ============================
# 5. main 진입점
# ============================
if __name__ == "__main__":
    run_bang_cli()
