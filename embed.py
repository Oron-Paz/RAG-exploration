from sentence_transformers import SentenceTransformer
import json

model = SentenceTransformer("all-MiniLM-L6-v2")

def get_passages_embeddings(path: str) -> tuple[list[str], list]:
    passages = []
    embeddings = []

    with open(path, "r") as f:
        for line in f:
            passage = json.loads(line)
            passages.append(passage["passage"])
            embeddings.append(model.encode(passage["passage"]))

    return (passages, embeddings)

if __name__ == "__main__":
    passages, embeddings = get_passages_embeddings("passages.json")
    for i in range(10):
        print(f"Passage {i}: {passages[i]}")
        print(f"Embedding {i}: {embeddings[i]}")
        print()
