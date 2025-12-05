import pandas as pd
from preprocess import preprocess_text
from embeddings import get_embedding
from vector_db import create_collection, upsert_vector
from search import semantic_search

CSV_PATH = "../data/digikala-comments.csv"

df = pd.read_csv(CSV_PATH, dtype=str)
comments = df["body"].fillna("").tolist()

create_collection("digikala_comments", dim=768)

for i, comment in enumerate(comments):
    comment_proc = preprocess_text(comment)
    vec = get_embedding(comment_proc)
    upsert_vector("digikala_comments", vec, payload={"comment": comment}, point_id=i)

queries = [
    "نظر در مورد کیفیت پایین دوربین در شب",
    "انتقاد از خدمات پس از فروش"
]

for q in queries:
    print(f"\nQuery: {q}")
    results = semantic_search(q, top_k=5)
    for idx, (payload, score) in enumerate(results):
        print(f"{idx+1}. Score: {score:.4f} | Comment: {payload['comment'][:100]}...")
