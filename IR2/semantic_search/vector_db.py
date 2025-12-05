from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance

qdrant = QdrantClient(":memory:")

def create_collection(name: str, dim: int = 768):
    qdrant.recreate_collection(
        collection_name=name,
        vectors_config=VectorParams(size=dim, distance=Distance.COSINE)
    )

def upsert_vector(collection_name: str, vector, payload: dict, point_id: int):
    qdrant.upsert(
        collection_name=collection_name,
        points=[{"id": point_id, "vector": vector.tolist(), "payload": payload}]
    )

def search_vector(collection_name: str, vector, top_k: int = 5):
    results = qdrant.search(
        collection_name=collection_name,
        query_vector=vector.tolist(),
        limit=top_k
    )
    return [(r.payload, r.score) for r in results]
