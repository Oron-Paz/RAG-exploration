# LangChain Course

A RAG (Retrieval-Augmented Generation) project built with LangChain, Anthropic Claude, and Qdrant vector database. Uses the [rag-mini-wikipedia](https://huggingface.co/datasets/rag-datasets/rag-mini-wikipedia) dataset from HuggingFace.

## Setup

1. Install dependencies with [uv](https://github.com/astral-sh/uv):
   ```bash
   uv sync
   ```

2. Copy `.env.example` to `.env` and fill in your API keys:
   ```bash
   cp .env.example .env
   ```

3. Download the dataset:
   ```bash
   uv run python load_dataset.py
   ```

4. Run the project:
   ```bash
   uv run python main.py
   ```

## Environment Variables

| Variable | Description |
|---|---|
| `ANTHROPIC_API_KEY` | Anthropic API key |
| `QDRANT_CLUSTER_API_KEY` | Qdrant Cloud API key |
| `QDRANT_CLUSTER_ENDPOINT` | Qdrant cluster URL |
