import os
from pathlib import Path
from langchain_community.document_loaders import (TextLoader , PyMuPDFLoader)
from dotenv import load_dotenv
from importlib.metadata import version
from langchain_anthropic import ChatAnthropic
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct, Document

load_dotenv()

# connect to Qdrant Cloud
client = QdrantClient(
    url = os.getenv("QDRANT_CLUSTER_ENDPOINT")
    api_key = os.getenv("QDRANT_CLUSTER_API_KEY")
    cloud_inference = True
)

print(f"Langchain-core version: {core_version}")
print(f"Langgraph version: {lg_version}")

def main():
    #llm = ChatAnthropic(model_name="claude-sonnet-4-5-20250929", temperature=0)
    #response = llm.invoke("say set up complete! in one word")
    #print(f"response: {response}")
    print("main")

if __name__ == "__main__":
    main()
