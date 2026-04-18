import json
import os
from pathlib import Path
from typing import Any

from langchain_huggingface import HuggingFaceEndpoint, HuggingFaceEmbeddings, ChatHuggingFace
from langchain_core.messages import SystemMessage
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from backend.web3_fetch_users import fetch_blockchain_users_structured

# ==============================
# STEP 1: LLM
# ==============================
load_dotenv(override=True)
llm = HuggingFaceEndpoint(
    repo_id="meta-llama/Llama-3.1-8B-Instruct",
    task="text-generation",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
)

model = ChatHuggingFace(llm=llm)

# ==============================
# STEP 2: OPTIONAL DB FILE (CACHE/DEBUG)
# ==============================
DB_FILE = Path(__file__).resolve().parent / "data" / "users.json"
DB_FILE.parent.mkdir(parents=True, exist_ok=True)

if not DB_FILE.exists():
    DB_FILE.write_text("[]\n", encoding="utf-8")


def load_users() -> list[dict[str, Any]]:
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_users(users: list[dict[str, Any]]) -> None:
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(users, f, indent=2, ensure_ascii=False)


def rag_text_from_user(user: dict[str, Any]) -> str:
    interests = user.get("interests") or []
    goals = user.get("goals") or []
    name = user.get("name") or "Unknown"

    interests_text = ", ".join(str(i) for i in interests) if interests else "None"
    goals_text = ", ".join(str(g) for g in goals) if goals else "None"

    return f"Name: {name}. Interests: {interests_text}. Goals: {goals_text}."

# ==============================
# STEP 3: EMBEDDINGS + VECTOR DB
# ==============================
embeddings = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)


def build_vectorstore(users: list[dict[str, Any]]):
    if not users:
        return None

    texts = [rag_text_from_user(u) for u in users]

    vectorstore = FAISS.from_texts(texts, embeddings)
    return vectorstore

# ==============================
# STEP 4: TAKE USER INPUT
# ==============================
def get_user_input():
    name = input("Enter your name: ")
    interests = input("Enter interests (comma separated): ").split(",")
    goals = input("Enter goals (comma separated): ").split(",")

    return {
        "name": name.strip(),
        "interests": [i.strip() for i in interests],
        "goals": [g.strip() for g in goals],
    }

# ==============================
# STEP 5: RAG RETRIEVAL STEP
# ==============================
def retrieve_candidates(new_user, vectorstore, k=3):
    query = f"""
    Interests: {new_user['interests']}
    Goals: {new_user['goals']}
    """

    results = vectorstore.similarity_search(query, k=k)
    return [r.page_content for r in results]

# ==============================
# STEP 6: LLM RANKING
# ==============================
def find_best_match(new_user, candidates):
    prompt = f"""
You are an AI matchmaking assistant for professional networking events.

New User:
Name: {new_user['name']}
Interests: {new_user['interests']}
Goals: {new_user['goals']}

Top Retrieved Candidates:
{json.dumps(candidates, indent=2)}

Instructions:
- Evaluate all given candidates
- Return exactly top 3 matches ranked from best to worst
- Weighting:
  - Interest similarity: 40%
  - Goal alignment: 30%
  - Vector DB relevance: 30%
- Score must be an integer from 0 to 100
- Each reason must be 20 to 30 words
- Return only valid JSON
- Do not include markdown
- Do not include any text outside JSON

Example output:
{{
  "matches": [
    {{
      "name": "rahul",
      "score": 88,
      "reason": "Strong overlap in AI and startup interests combined with identical networking goals creates high alignment. Vector similarity shows closely related profiles."
    }},
    {{
      "name": "ananya",
      "score": 84,
      "reason": "Shared interest in AI and machine learning with compatible collaboration goals makes this a relevant match. Vector retrieval suggests meaningful contextual similarity."
    }},
    {{
      "name": "neha",
      "score": 78,
      "reason": "Common focus on AI-related domains and partially aligned goals creates a useful connection. Vector relevance indicates moderate similarity and practical networking value."
    }}
  ]
}}
"""

    response = model.invoke([SystemMessage(content=prompt)])
    return response.content

# ==============================
# STEP 7: MAIN FLOW
# ==============================
def main():
    print("\n--- RAG AI Event Matchmaker (Blockchain + Vector DB) ---\n")

    print("Fetching users from blockchain...\n")

    try:
        users = fetch_blockchain_users_structured()
    except Exception as exc:  # noqa: BLE001
        print("Failed to fetch blockchain users.")
        print(f"Details: {exc}")
        return

    if not users:
        print("No users fetched from blockchain.")
        return

    save_users(users)
    vectorstore = build_vectorstore(users)

    if not vectorstore:
        print("No users available for vector database.")
        return

    new_user = get_user_input()

    print("\nRetrieving similar users...\n")

    candidates = retrieve_candidates(new_user, vectorstore, k=3)

    print("\nRanking with LLM...\n")

    result = find_best_match(new_user, candidates)

    print("\n=== RESULT ===")
    print(result)

    print(f"\nSaved users to: {DB_FILE}")

if __name__ == "__main__":
    main()