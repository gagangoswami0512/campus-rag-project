from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"
model = SentenceTransformer(MODEL_NAME)

def create_embeddings(chunks):
    texts = [chunk["text"] for chunk in chunks]

    embeddings = model.encode(texts)
    return embeddings

if __name__ == "__main__":
    from ingest import load_pdfs
    from chunks import split_text

    docs = load_pdfs()
    chunks = split_text(docs)

    vector = create_embeddings(chunks)

    print("Embeddings shape:", vector.shape)
    print("Total Embeddings:", len(vector))
    print("Total Chunks:", len(chunks))

    