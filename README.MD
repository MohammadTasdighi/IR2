## Sentence Embedding Method (CLS vs. Mean Pooling)

In this project, we adopt **Mean Pooling** as the method for generating the unified embedding vector for each comment and query.

### Why Mean Pooling?

- In models like **ParsBERT**, the **CLS token is optimized mainly for classification tasks**, not for semantic representation.  
  As a result, CLS embeddings tend to be **task-dependent**, sometimes noisy, and often fail to capture full sentence meaning.
- **Mean Pooling incorporates all token embeddings**, allowing the final vector to reflect the *entire semantic content* of the sentence rather than relying on a single token.
- Empirically, Mean Pooling provides **higher stability**, **better generalization**, and **more accurate similarity scoring** in retrieval and semantic search tasks.
- Most state-of-the-art retrieval systems based on BERT variants also prefer Mean Pooling unless a model is explicitly fine-tuned for CLS-based embedding (which ParsBERT is not).

For these reasons, Mean Pooling delivers **more reliable**, **context-rich**, and **discriminative** embeddings, making it the preferred choice for the semantic search pipeline in this project.
