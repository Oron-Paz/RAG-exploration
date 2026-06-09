import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from embed import get_passages_embeddings

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_CLUSTER_ENDPOINT"),
    api_key=os.getenv("QDRANT_CLUSTER_API_KEY"),
)

def upload(path: str, collection_name: str):
    passages, embeddings = get_passages_embeddings(path)

    if not client.collection_exists(collection_name):
        client.create_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(size=384, distance=Distance.COSINE)
        )

    points = [
        PointStruct(id=i, vector=embeddings[i].tolist(), payload={"text": passages[i]})
        for i in range(len(passages))
    ]
    
    # need to upload in batches qdrant wasnt happy with the bulk upload :(
    batch_size = 100
    for i in range(0, len(points), batch_size):
        client.upsert(collection_name=collection_name, points=points[i:i+batch_size])
        print(f"Upserted {min(i+batch_size, len(points))}/{len(points)}")

    print(f"Done — {len(points)} points uploaded to '{collection_name}'")

if __name__ == "__main__":
    upload("passages.json", "wikipedia")
