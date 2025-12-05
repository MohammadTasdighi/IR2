import os, sys
import pandas as pd
from elasticsearch import Elasticsearch, helpers
from persiantools.jdatetime import JalaliDate

CSV_PATH = os.getenv("CSV_PATH", "../data/digikala-comments.csv")
INDEX_NAME = os.getenv("INDEX_NAME", "digikala_comments")
ES_HOST = os.getenv("ES_HOST", "http://localhost:9200")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", "400"))
BULK_CHUNK = int(os.getenv("BULK_CHUNK", "200"))

es = Elasticsearch(ES_HOST)

def normalize_date(date_str):
    if pd.isna(date_str) or str(date_str).strip() == "":
        return None
    try:
        parts = [int(p) for p in str(date_str).split("-")]
        if len(parts) == 3:
            return str(JalaliDate(parts[0], parts[1], parts[2]).to_gregorian())
    except:
        return None
    return None

def gen_actions(df_chunk):
    for _, row in df_chunk.iterrows():
        doc = {
            "title": "" if pd.isna(row.get("title")) else str(row.get("title")),
            "body": "" if pd.isna(row.get("body")) else str(row.get("body")),
            "advantages": "" if pd.isna(row.get("advantages")) else str(row.get("advantages")),
            "disadvantages": "" if pd.isna(row.get("disadvantages")) else str(row.get("disadvantages")),
            "created_at": normalize_date(row.get("created_at"))
        }
        yield {
            "_index": INDEX_NAME,
            "_id": int(row["id"]) if pd.notna(row.get("id")) else None,
            "_source": doc
        }

def main():
    if not os.path.exists(CSV_PATH):
        print(f"CSV file not found: {CSV_PATH}", file=sys.stderr)
        sys.exit(1)

    total_indexed = 0
    for i, chunk in enumerate(pd.read_csv(CSV_PATH, chunksize=CHUNK_SIZE, iterator=True, dtype=str, low_memory=True)):
        success, _ = helpers.bulk(es, gen_actions(chunk), chunk_size=BULK_CHUNK, request_timeout=120, max_retries=3)
        total_indexed += success
        print(f"[chunk {i}] indexed so far: {total_indexed}")

    print(f"Finished. Total indexed: {total_indexed}")

if __name__ == "__main__":
    main()
