# SKN11-4TH-3Team
- 주제 : LLM 기반 보드게임 룰 설명 & 맞춤형 추천 챗봇 구동 웹 어플리케이션 개발
- 개발기간 : 25.05.16~25.06.11
---
## 📑 Index

1. [팀 소개](#1-팀-소개)
2. [Overview](#2-overview)
3. [기술 스택](#3-기술-스택)
4. [시스템 아키텍처](#4-시스템-아키텍처)
5. [WBS](#5-wbs)
6. [요구사항 명세서](#6-요구사항-명세서)
7. [수집한 데이터 및 전처리 요약](#7-수집한-데이터-및-전처리-요약)
8. [DB 연동 구현 코드](#8-db-연동-구현-코드-링크)
9. [테스트 계획 및 결과 보고서](#9-테스트-계획-및-결과-보고서)
10. [성능 개선 노력](#10-성능-개선-노력)
11. [추후 개선점](#11-추후-개선점)
12. [한 줄 회고](#12-한-줄-회고)


## 1. 팀 소개
### 팀명 : BoardNavi
- Board + Navi의 합성어로, “보드게임 세계의 길잡이” 라는 뜻으로, 사용자가 보드게임이라는 낯선 세계에서 길을 잃지 않도록 규칙과 추천을 안내해주는 팀이라는 의미를 담고 있습니다. 


### 👤 팀원
![image](https://github.com/user-attachments/assets/dd3dbf0d-d5e6-4754-ba53-2bb43ccb3bf5)

<table>
  <tr>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/f85c63c4-9587-430a-875e-22160c64e311" width="120" />
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/074a0877-1279-4d80-83bc-98d4eac64ee0" width="120" />
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/ec4fcead-4222-49ea-87fa-e9272894ded6" width="120" />
    </td>
    <td align="center">
      <img src="https://github.com/user-attachments/assets/e5b7621f-11e9-42c0-959f-86100ad959ee" width="120" />
    </td>
  </tr>
  <tr>
    <td align="center">
      <a href="https://github.com/Kimjeongwon12">김정원</a>
    </td>
    <td align="center">
      <a href="https://github.com/minjung2266">이민정</a>
    </td>
    <td align="center">
      <a href="https://github.com/Minor1862">정민호</a>
    </td>
    <td align="center">
      <a href="https://github.com/junoaplus">황준호</a>
    </td>
  </tr>
</table>
<br/>


## 2. Overview

  #### 📖 프로젝트 소개 
보드게임 봇 "🤖보비"는 보드게임 룰 설명과 추천 기능을 제공하는 LLM 기반 챗봇입니다. 챗봇은 사용자의 질문에 따라 게임 규칙을 설명하거나 취향에 맞는 게임을 추천해줍니다.

#### ⭐ 프로젝트 필요성
<table>
  <tr>
    <td>초보자들의 게임 선택 장애</td>
    <td>보드게임의 대중화로 다양한 게임이 출시되고 있지만, 초보 이용자들은 복잡한 룰을 이해하거나 자신의 취향에 맞는 게임을 고르는 데 어려움을 겪음</td>
  </tr>
  <tr>
    <td>보드게임 카페의 인력 문제</td>
    <td>보드게임 카페에서는 다양한 게임을 설명하고 추천할 수 있는 직원을 필요로 하지만, 폭넓은 게임 지식을 갖춘 인력을 채용하기란 쉽지 않음</td>
  </tr>
</table>

#### 🎯 프로젝트 목표

<table>
  <tr>
    <td>보드게임 룰 설명 챗봇 구현</td>
    <td>사용자의 질문에 정확하고 간결한 게임 규칙을 제공</td>
  </tr>
  <tr>
    <td>보드게임 추천 기능 제공</td>
    <td>게임 방법, 인원 수, 테마 등을 기반으로 유사도 분석을 통해 최적의 보드게임을 추천</td>
  </tr>
  <tr>
    <td>도메인 특화 지식 반영</td>
    <td>벡터DB 구축과 LLM 파인튜닝을 통해 보드게임에 특화된 지식 기반 챗봇 구축</td>
  </tr>
</table>

<hr>

## 3. 기술 스택

| 항목                | 내용 |
|---------------------|------|
| **Language**        | ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) |
| **Development**     | ![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)<br>![Colab](https://img.shields.io/badge/Google%20Colab-F9AB00?style=for-the-badge&logo=googlecolab&logoColor=white)<br>![RunPod](https://img.shields.io/badge/RunPod-8A2BE2?style=for-the-badge) |
| **Crawler** | ![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-4B8BBE?style=for-the-badge&logo=python&logoColor=white) |
| **Embedding Model** | ![Hugging Face](https://img.shields.io/badge/HuggingFace-FFD21F?style=for-the-badge&logo=huggingface&logoColor=black) |
| **Vector DB**       | ![FAISS](https://img.shields.io/badge/FAISS-009688?style=for-the-badge) |
| **LLM Model**       | ![gpt-3.5-turbo](https://img.shields.io/badge/gpt--3.5-4B91FF?style=for-the-badge&logo=openai&logoColor=white) |
| **Demo**            | ![Gradio](https://img.shields.io/badge/Gradio-FF4B4B?style=for-the-badge&logo=gradio&logoColor=white) |
| **Collaboration Tool** | ![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)


## 4. 시스템 아키텍처

![diagram](https://github.com/user-attachments/assets/f3a87011-9285-41a3-9932-b20db7992b11)

1. 질문 입력
→ 원하는 서비스에 따라 user가 질문 입력 

2. 문서 검색
→ Retriver가 받은 질문을 임베딩 후, FAISS를 통해 유사한 문장을 질의 

3. Prompt 구성 
→ 검색된 정보를 기반으로 LLM에게 전달할 Prompt 구성 

4. 모델 응답 생성
→ Prompt가 Fine-Tuning된 모델에게 전달되어 응답을 생성

5. 생성된 답변을 User에게 반환
→ LLM이 생성한 답변이 사용자에게 전달


## 5. WBS(수정)
![image](https://github.com/user-attachments/assets/edcfd623-1383-48dd-a661-5110a4a31204)


## 6. 요구사항 명세서(수정)
![image](https://github.com/user-attachments/assets/a5f797f5-77cf-4c94-99f2-51373c47e440)


## 7. 수집한 데이터 및 전처리 요약
### 데이터 수집

  - 본 프로젝트에서는 225개의 게임 정보들이 적혀있는 [보드게임 블로그 사이트](https://blog.naver.com/mukjjippa_boardgame)에서 게임 관련 데이터를 크롤링하였습니다.

```
def download_naver_blog_content(url, save_folder):
    response = requests.get(url, headers=USER_AGENT)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 제목 추출
    title = soup.select_one('meta[property="og:title"]')
    if title:
        game_name = re.sub(r'[\\/*?:"<>|]', "", title['content'])[:50]
    
    # 본문 추출
    content_area = soup.select_one('div.se-main-container')
    content_text = content_area.get_text().strip() if content_area else "내용 없음"
    
    # 파일 저장
    save_path = os.path.join(save_folder, f"{game_name}.txt")
    with open(save_path, 'w', encoding='utf-8') as f:
        f.write(content_text)

```


### 데이터 전처리
✅ **원본 데이터 전처리** 
- 전처리 형식

| 원본 형태                             | 변환 방식                                          |
|----------------------------------|-------------------------------------------------|
| `@`, `☆`와 같은 특수문자                              | → 모두 제거                               |
| `- 2 인 -`, `- 4 인 -` 등               | → `2인일 시:`, `4인일 시:` 형태로 변환                    |
| 2~4인        | → `인`을 제거 / player 정보가 없을 시 ~로 처리 |
| 전체 문장 띄어쓰기 및 맞춤법               | → 맞춤법 교정, 불필요한 공백 제거, 문장부호 보정 적용              |


- 전처리 전 / 후

```
  [{
    "id": "블로커스_보드게임",
    "game_name": "블로커스 보드게임",
    "section": "RULES",
    "text": "게임 의 목적 - 하나라도 많은 블록을 놓으세요 게임 종료 시점 - 게임 플레이 어 모두가 더 이 상 블록을 놓지 못하는 상황이 되면 게임 종료이 며 남은 블록의 면적이 가 장 작은 플레이 어가 승리합니다 블록의 네모를 세서 면적을 계산하세요 게임 플레이 @자신의 차례가 되면 블록을 1 개 놓으면차례가 넘어갑니다@자신의 첫 블록은 모서리의 면을 채워야 합니다 @같은 색상의 블록은 꼭짓점이 닿아야 합니다 같은 색상의 블록은 면이 닿을 수 없습니다 게임 세팅 - 4 인 - 원하는 색상의 블록 조각을 21 개씩 1 가 지 색상으로 가 져갑니다 3 인 - 1 가 지 색상을 가 져가 고 남은 1 가 지 색상의 차례에 는 돌아가 면서 블록을 놓습니다 (4 인이 랑 같은 방식인데 1 명의 역할을 3 명이 합니다) 2 인 - 2 가 지 색상의 블록을 총 42 개 가 져옵니다 4 인 플레이 와 같은 방식으로 진행합니다 ☆블로 커스는 2 인용이 따로 있습니다 이 상 블로 커스 보드게임 규칙 (2~4 인) 이 었습니다",
    "source_file": "블로커스 보드게임 규칙(2~4인)",
    "players": "2~4인"
  },
...
```

```
[{
  "id": "블로커스_보드게임",
  "game_name": "블로커스 보드게임",
  "section": "RULES",
  "text": "게임의 목적: 하나라도 많은 블록을 놓는 것입니다. 게임 종료 시점: 모든 플레이어가 더 이상 블록을 놓지 못하는 상황이 되면 게임이 종료되며, 남은 블록의 면적이 가장 작은 플레이어가 승리합니다. 블록의 네모 칸 수를 세어 면적을 계산하세요. 게임 플레이: 자신의 차례가 되면 블록을 1개 놓고 차례를 넘깁니다. 첫 블록은 반드시 모서리에 닿도록 놓아야 합니다. 같은 색상의 블록은 꼭짓점만 닿아야 하며, 면이 닿으면 안 됩니다. 게임 세팅: 4인일 시: 원하는 색상의 블록 조각 21개를 하나씩 선택합니다. 3인일 시: 각자 1가지 색상의 블록을 가져가고, 남은 1가지 색상의 차례에는 돌아가면서 블록을 놓습니다. (4인 방식과 동일하나, 한 명의 역할을 3명이 번갈아 합니다) 2인일시: 두 가지 색상의 블록을 총 42개 가져와 4인 플레이 방식과 동일하게 진행합니다.  블로커스는 2인 전용 버전도 별도로 존재합니다.",
  "players": "2~4"
}]
```

✅ **vectorDB 전처리**
-  게임 추천 기능 : 원본 데이터 전처리와 동일하게 진행함. 


- 게임 룰 설명 기능 : 설명 단위로 청크하여 전처리 진행함.
  ```
  "블로커스": {
    "game_name": "블로커스",
    "chunks": [
      "게임의 목적: 하나라도 많은 블록을 놓는 것입니다.",
      "게임 종료 시점: 모든 플레이어가 더 이상 블록을 놓지 못하는 상황이 되면 게임이 종료되며, 남은 블록의 면적이 가장 작은 플레이어가 승리합니다. 블록의 네모 칸 수를 세어 면적을 계산하세요. 게임 플레이: 자신의 차례가 되면 블록을 1개 놓고 차례가 넘어갑니다. 첫 블록은 반드시 모서리에 닿도록 놓아야 합니다. 같은 색상의 블록은 꼭짓점이 닿아야 하며, 면이 닿으면 안 됩니다. 게임 세팅: 4인일 시: 원하는 색상의 블록 조각을 21개씩 하나씩 가져갑니다. 3인일 시: 각자 1가지 색상의 블록을 가져가고, 남은 1가지 색상의 차례에는 돌아가면서 블록을 놓습니다. (4인 방식과 동일하나,  한 명의 역할을 3명이 번갈아 합니다.) 2인일 시: 두 가지 색상의 블록을 총 42개 가져와 4인 플레이 방식과 동일하게 진행합니다. 블로커스는 2인 전용 버전도 별도로 존재합니다.."
    ]
  }
  ```


✅ **finetunning 전처리**
- 전처리 전 / 후
```
[
  {
    "prompt": "이 게임의 전체적인 진행 흐름을 처음부터 끝까지 알려줄 수 있을까?",
    "completion": ""
  },
  {
    "prompt": "그중에서 승리 조건이 이해가 잘 안돼. 다시 자세히 설명해줄래?",
    "completion": ""
  },
```

```
    {
        "prompt": "게임명: 스플렌더\n질문: 이 게임에서 각각의 역할은 어떻게 돼?\nRULES: 게임의 목적: 점수가 높은 사람이 승리. 게임 종료 시점: 15점 이상을 낸 사람이 있을 시 그 턴이 마지막 턴이 된다. 점수가 같을 때는 카드가 적은 사람이 승리. 점수를 내는 방법은 개발카드 or 귀족 타일을 가져오면 됨. 왼쪽 상단의 숫자가 점수를 뜻함. 게임 세팅: 1, 2, 3단계 개발카드를 4장씩 12장 깔아줍니다. 5종류의 보석과 귀족 타일을 인원수에 맞게. 2인일시: 보석 4개씩, 귀족 타일 3개, 황금 토큰(조커) 5. 3인일시: 보석 5개씩, 귀족 타일 4개, 황금 토큰 5개. 4인일시: 보석 7개씩, 귀족 타일 5개, 황금 토큰 5개. 게임 진행: 내 차례가 되면 3가지의 행동 중 1개를 할 수 있다. 1. 보석 가져오기 (황금 토큰 제외 5가지의 보석 중). 1가지의 보석을 2개 가져오기 (단, 가져오려는 보석이 4개 이상이어야 함). 3가지의 보석을 1개씩 3개 가져오기. 내가 보유할 수 있는 보석의 개수는 조커를 포함해 10개까지만 가질 수 있다. 2. 개발 카드 가져오기: 개발 카드 왼쪽 하단에 필요한 보석의 종류와 개수가 있는데 보석을 그만큼 반납하고 가져올 수 있다. 카드를 가져오며 빈자리는 새로운 카드로 대체한다. 가져온 개발 카드는 개발 카드 오른쪽 상단에 있는 보석 1개의 역할을 한다. 개발 카드 구매 시 필요한 보석 수가 그만큼 줄어듦. 3. 찜하기: 황금 토큰 1개를 가져올 수 있으며 개발카드 1장을 찜할 수 있다. 찜한 카드는 다음 턴부터 나만 구입할 수 있다. 3장까지의 찜한 카드를 보유할 수 있다. 찜한 카드가 3장일시 찜하기를 하지 못한다. ☆ 귀족 카드 가져오기 (보석으로 구매 X): 귀족 카드는 귀족 카드에 표시된 개발 카드를 모두 모으면 가져올 수 있다. 내 차례를 소진하지 않으며 개발 카드를 모아 먼저 가져오는 사람이 임자 (개발 카드 반납 X).",
        "completion": "게임명: 스플렌더\n\n게임의 목적은 점수가 높은 사람이 승리하는 것입니다. 게임 종료 시점은 한 플레이어가 15점 이상을 달성했을 때이며, 그 턴이 마지막 턴이 됩니다. 동점일 경우, 카드 수가 적은 플레이어가 승리합니다. \n\n게임에서 점수를 획득하는 방법은 개발카드를 가져오거나 귀족 타일을 획득하는 것입니다. 왼쪽 상단의 숫자가 카드의 점수를 나타냅니다.\n\n게임을 시작할 때는 1, 2, 3단계의 개발카드를 각각 4장씩 12장을 깔아줍니다. 또한 플레이어 인원수에 따라 5종류의 보석과 귀족 타일을 나눠줍니다. \n\n2명 플레이 시: 보석 4개, 귀족 타일 3개, 황금 토큰(조커) 5개\n3명 플레이 시: 보석 5개, 귀족 타일 4개, 황금 토큰 5개\n4명 플레이 시: 보석 7개, 귀족 타일 5개, 황금 토큰 5개\n\n게임 진행은 각 플레이어의 차례마다 3가지 행동 중 1가지를 선택하여 수행합니다. \n1. **보석 가져오기**: 5가지의 보석 중 1가지 보석을 2개 가져오거나, 3가지의 보석을 1개씩 3개 가져올 수 있습니다. 단, 보유 가능한 보석 수는 조커를 포함하여 최대 10개까지입니다.\n2. **개발 카드 가져오기**: 개발 카드에 표시된 필요한 보석의 종류와 개수를 반납하고 가져올 수 있습니다. 새로운 카드로 대체됩니다. 가져온 개발 카드는 오른쪽 상단의 보석 1개를 대체합니다. \n3. **찜하기**: 황금 토큰 1개를 가져오거나 개발카드 1장을 찜할 수 있습니다. 찜한 카드는 다음 턴부터 구입할 수 있습니다. 최대 3장까지 찜한 카드를 보유할 수 있습니다.\n\n또한, 귀족 카드를 획득하는 방법은 보석으로 구매하는 것이 아닌 특정 개발 카드를 모아야 합니다. 귀족 카드를 모은 플레이어는 개발 카드 반납 없이 귀족 카드를 획득할 수 있습니다. \n\n이렇게 게임을 진행하여 15점 이상을 달성한 플레이어가 나오면 해당 턴을 마지막 턴으로 하여 게임이 종료됩니다. 가장 높은 점수를 획득한 플레이어가 이 게임의 승자가 됩니다."
    },
```

## 8. DB 연동 구현 코드 (링크)
- DB 연동 구현 코드 : [url](https://drive.google.com/drive/folders/1ggLn33w5k5kioylWpcgxgDyhC-NQ5W_3?usp=sharing)


## 9. 테스트 계획 및 결과 보고서
[테스트_계획_및_결과_보고서](테스트_계획_및_결과_보고서.pdf)

### 기능 1. 유사도 기반 게임 추천
#### 🎯 상황별 질문 

| 상황 | 캡처 이미지 |
|------|-------------|
| 전략 게임 추천 요청 | ![전략 게임 추천](https://github.com/user-attachments/assets/e9bf97dc-ecca-4f97-b182-cb69eb4429a2) | 
| 쉬운 카드게임 추천 요청 | ![쉬운 카드게임 추천](https://github.com/user-attachments/assets/cc092575-8174-4205-a8a7-75934d256458) | 
| 다양한 추천 요청 | ![다양한 추천](https://github.com/user-attachments/assets/3f46649e-c980-4bbe-9346-98ff8197676a) |
| 룰 설명 요청 | ![룰 설명](https://github.com/user-attachments/assets/0f53f99f-a7e6-4e37-b040-b22444661eec) |


### 기능 2. 게임 룰 설명
#### 🎯 세부적인 질문 예시

| 상황 | 캡처 이미지 |
|------|-------------|
| 특정 게임 내 점수 계산 질문 | ![점수 계산 질문](https://github.com/user-attachments/assets/2c53bcc1-f098-4a59-ae3c-a50c2c19f43f) |
| 카드 사용 조건 질문 | ![카드 조건 질문](https://github.com/user-attachments/assets/5cd94b44-ff60-4040-b440-56ff44491c2e) |
| 게임 진행 중 행동 가능 여부 질문 | ![행동 가능 여부](https://github.com/user-attachments/assets/fce9bb43-7ef1-4a4e-8800-1f8e8a83072e) |
| 규칙 예외 상황 질문 | ![예외 상황 질문](https://github.com/user-attachments/assets/26abde1a-5014-4fa4-8e02-19e51b1317d7) |


## 10. 성능 개선 노력
1. **목적에 따른 벡터DB 분리** : 추천 기능과 룰 설명 기능이 요구하는 정보가 달라 벡터DB를 별도로 구축함으로써, 검색 정확도를 높임

2. **RAG 모델 실험** :
다양한 llm 모델 (openchat, tinyllama, koalphaca)를 비교하여 응답 성능을 개선

3. **fine tunning 성능 개선**

   **[파인튜닝 모델]**
  - base model: gpt-3.5-turbo-0125
  - training method: Supervised Fine-Tuning (SFT)
  - train token: 3,992,712 tokens
  - output model : ft:gpt-3.5-turbo-0125:tset::BX2RnWfq

    ![image](https://github.com/user-attachments/assets/36490fa2-4300-4a99-9a83-1e4741a53bb0)
    ![image](https://github.com/user-attachments/assets/78db9bd9-6ee4-4c2d-a3c6-177ce2176685)


  
  초기에는 한국어에 특화된 오픈소스 모델인 KoAlpaca를 활용해 파인튜닝을 진행하였으나, 실제 추론 결과에서 질문과 무관한 답변을 생성하거나, 규칙과 동떨어진 응답을 출력하는 문제가 발생하였습니다.
  ```
  # koAlpaca 사용
  [질문]: 이 게임의 규칙을 설명해줘
  [최종 응답]: 이 게임은 가족들과 함께하는 따뜻한 보드게임입니다. 카드를 섞고 나누며 서로의 감정을 나누는 것이 핵심입니다. 승패보다는 모두가 즐겁게 참여하는 것이 중요합니다. 점수를 계산할 필요는 없으며, 규칙은 자유롭게 정하면 됩니다. 웃음과 배려가 가장 중요한 규칙입니다.
  ```
  이에 따라 안정적인 언어 이해 및 규칙 기반 응답 생성을 위해 gpt-3.5-turbo를 활용한 파인튜닝을 진행했습니다.
  ```
  # gpt3.5-turbo 사용
  [최종 응답]: 이 게임은 '뱅'이라는 서부 총격전을 소재로 한 보드게임입니다. 게임의 목적은 보안관, 부관, 무법자, 배신자 중 누군가가 목표를 이루면 게임에서 승리하게 됩니다. 총알 토큰(생명)을 모두 잃은 사람은 게임에서 탈락하게 됩니다. 
  (중략)
  ...
  ```
  
  ```  
  # 파인튜닝 설정
  training_args = TrainingArguments(
      output_dir='./fine_tuned_model',
      num_train_epochs=5,
      per_device_train_batch_size=2,
      gradient_accumulation_steps=8,
      learning_rate=5e-5,
      fp16=True,
      logging_dir='./logs',
      logging_steps=10,
      save_steps=500,
      save_total_limit=3,
  )
  
  ```

## 11. 추후 개선점
#### 1. 사용자 인터렉션 강화
- 꼬리질문 대응을 위해 세션 상태 유지
- 자주 선택한 게임 유형을 저장해 개인화 추천 강화

#### 2. 데이터 품질 개선
- 게임 정보 크롤링 자동화를 통해 최근 게임 업데이트


#### 3. 모델 성능 향상
- 비용 절감을 위해 다른 모델 적용 방법을 모색
- 꼬리질문 대응에 특화된 LoRA 개선

## 12. 한 줄 회고                                                                                                               
>  김정원 : LLM을 사용만 해보고 개발하는 것은 처음이라 관련 지식들을 처음 접하는 것이 많았습니다. 이번 프로젝트를 진행하면서 개발 프로세스를 어떻게 잡아야 하는지, 수많은 임베딩, RAG, LLM 모델 중에서 어떤 모델을 사용해야 우리의 프로젝트 결과물에 가장 우수한 성능을 낼 수 있는지 알 수 있었습니다. GPU 자원과 시간이 한정적이라 A-Z로 완벽히 구축하지 못한 것 같아 아쉽지만 이후에 어떻게 발전시킬 지 생각해 볼 수 있었던 시간이었습니다. 
>
> 이민정 : 여러 모델을 바꿔가며 RAG의 성능을 확인하는 과정에서 단순히 성능이 좋다는 모델보다는 내가 필요한 목적에 따라 알맞게 모델을 선택해야 함을 알게 되었습니다. 또 gpu 자원과 시간이 한정되어 있어 여러번 테스트 해보지 못한 점이 아쉬움이 남습니다.
>
>  정민호 : 수업에서 배운 LLM 분야를 직접 응용해볼 수 있어 의미있는 경험이 된것 같습니다.                                                                                
>
>  황준호 : 여러 모델을 파인튜닝 해보면서 모델마다 설정해줘야 할 것도 다르고 시간도 다르고 방법도 달라서 어려웠습니다. 하지만 파인튜닝만 5번 이상을 해보면서 점점 손에 익어가는 유익한 시간이었습니다.

