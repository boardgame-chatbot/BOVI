# game_recommend.py

import json
import faiss
import numpy as np
import re
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from huggingface_hub import login
# login("토큰입력")

# ✅ Kanana LLM 세팅
MODEL_NAME = "kakaocorp/kanana-1.5-2.1b-instruct-2505"  # beomi/KoAlpaca-Polyglot-5.8B
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME, device_map="auto", torch_dtype="auto")
llm_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=768)

# ✅ 데이터 및 벡터DB 로드
index = faiss.read_index("data/game_index.faiss")

with open("data/texts.json", "r", encoding="utf-8") as f:
    texts = json.load(f)

with open("data/game_names.json", "r", encoding="utf-8") as f:
    game_names = json.load(f)

embed_model = SentenceTransformer("BAAI/bge-m3", device="cuda")

def clean_output(raw_output: str) -> str:
    if "추천 완료!" in raw_output:
        raw_output = raw_output.split("추천 완료!")[0]
    return raw_output.strip()

def recommend_games_with_rag(query, top_k=3):
    """
    사용자 자연어 질의(query)에 따라 유사도 기반 보드게임 추천 (Kanana LLM + VectorDB)
    """
    number_match = re.search(r'(\d+)\s*개', query)
    top_k = int(number_match.group(1)) if number_match else top_k

    query_embedding = embed_model.encode([query], normalize_embeddings=True)
    _, indices = index.search(np.array(query_embedding), k=top_k)

    retrieved_games = []
    name_list = []
    for idx in indices[0]:
        name = game_names[idx]
        desc = texts[idx]
        retrieved_games.append(f"[{name}]\n{desc}")
        name_list.append(f"- {name}")

    context = "\n\n".join(retrieved_games)
    name_list_str = "\n".join(name_list)

    prompt = f"""아래는 보드게임 설명입니다. 각 게임은 "[게임명]\n설명" 형식으로 되어 있습니다.

[게임 설명]
{context}

⚠️ 반드시 아래의 게임 이름 목록 중에서만 선택할 수 있습니다. 이 목록에 없는 게임 이름을 절대 생성하지 마세요.
[허용된 게임 이름 목록]
{ name_list_str }

[사용자 질문]
{query}

📌 출력 지침:
- 반드시 위 목록에 있는 게임 중에서만 {top_k}개를 골라 추천하세요.
- 출력 형식은 반드시 아래 형식처럼 작성하세요:

게임명1: 추천 이유
게임명2: 추천 이유
게임명3: 추천 이유

- 각 줄은 '게임명: 추천 이유' 형식으로만 작성하고, 줄바꿈 이외에 아무 포맷도 쓰지 마세요.
- 추천이 모두 끝나면 마지막 줄에 반드시 다음과 같이 써주세요:
추천 완료!
그 이후에는 아무 것도 쓰지 마세요.
"""

    # Kanana LLM 호출
    raw_output = llm_pipeline(prompt)[0]["generated_text"]
    cleaned = clean_output(raw_output)

    return cleaned

# 테스트
if __name__ == "__main__":
    user_query = "네 명이 할 수 있는 파티 게임 3개 추천해줘"
    print(recommend_games_with_rag(user_query))
