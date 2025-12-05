from preprocess import preprocess_text
from embeddings import get_embedding
from vector_db import search_vector

def semantic_search(query: str, top_k: int = 5):
    query_proc = preprocess_text(query)
    query_vec = get_embedding(query_proc)
    results = search_vector("digikala_comments", query_vec, top_k)
    return results
