from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)


def create_embeddings(chunks: list):

    embeddings = embedding_model.encode(
        chunks,
        convert_to_numpy=True
    )

    return embeddings