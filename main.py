import os
from dotenv import load_dotenv
from langchain_anthropic import ChatAnthropic
from qdrant_client import QdrantClient

load_dotenv()

client = QdrantClient(
    url=os.getenv("QDRANT_CLUSTER_ENDPOINT"),
    api_key=os.getenv("QDRANT_CLUSTER_API_KEY"),
)

def main():
    pass

if __name__ == "__main__":
    main()
