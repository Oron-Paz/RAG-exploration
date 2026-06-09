from datasets import load_dataset

ds = load_dataset("rag-datasets/rag-mini-wikipedia", "text-corpus")
ds["passages"].to_json("passages.json")

ds_testing = load_dataset("rag-datasets/rag-mini-wikipedia", "question-answer")
ds_testing["test"].to_json("questions.json")
