
## Dataset Subsampling for Feasibility

Due to the **large size of the Digikala comments dataset**, processing the entire CSV on a standard CPU would take **several days** to compute embeddings and index all vectors in Qdrant.  

To ensure **practical execution** and **demonstration of results**, we limited the pipeline to the **first 200,000 records**. This approach allows us to:

- Quickly validate the **semantic search workflow**.
- Demonstrate **retrieval accuracy and relevance** without the full dataset.
- Maintain **reasonable memory usage** and **runtime** on a typical CPU setup.

For production or full-scale evaluation, it is recommended to run the pipeline on a **GPU-enabled environment** and process the dataset in **batches** to handle the complete data efficiently.
