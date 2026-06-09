import os
import json
import anthropic
from qdrant_client import QdrantClient
from dotenv import load_dotenv
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
load_dotenv()
test_questions_path = "questions.json"

qdrant = QdrantClient(
    url=os.getenv("QDRANT_CLUSTER_ENDPOINT"),
    api_key=os.getenv("QDRANT_CLUSTER_API_KEY"),
)
claude = anthropic.Anthropic()


def ask_claude(question: str, passage: str) -> str:
    response = claude.messages.create(
        model="claude-haiku-4-5",
        max_tokens=16,
        messages=[{
            "role": "user",
            "content": f"Answer in as few words as possible using only the passage. If the passage is irrelevant to the question or doesn't contain the answer, say exactly 'I don't know'.\n\nPassage: {passage}\n\nQuestion: {question}"
        }]
    )
    return response.content[0].text.strip().lower()


def main():
    correct_count = 0
    total = 0

    with open(test_questions_path, "r") as f:
        for line in f:
            content = json.loads(line)
            question = content["question"]
            true_answer = content["answer"].strip().lower()
            total += 1

            result = qdrant.query_points(
                collection_name="wikipedia",
                query=embedding_model.encode(question).tolist(),
                with_payload=True,
                limit=1
            )
            passage = result.points[0].payload["text"]
            answer = ask_claude(question, passage)

            if true_answer in answer or answer in true_answer:
                correct_count += 1

            if total % 10 == 0:
                print(f"\n--- Question {total} ---")
                print(f"Q: {question}")
                print(f"Passage: {passage}")
                print(f"Model answer: {answer}")
                print(f"True answer:  {true_answer}")

    print(f"\nCorrect = {correct_count}")
    print(f"Incorrect = {total - correct_count}")
    print(f"Accuracy = {correct_count / total:.2%}")

if __name__ == "__main__":
    main()
