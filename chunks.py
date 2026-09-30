from ingest import load_pdfs
def split_text(documents, chunk_size=500, overlap=100):
    chunks = []

    for doc in documents:
        start = 0
        text = doc["text"]

        while start < len(text):
            end = start + chunk_size
            chunk_text = text[start:end]

            chunks.append({
                "filename": doc["filename"],
                "page_number": doc["page_number"],
                "text": chunk_text,
            })

            start += chunk_size - overlap

    return chunks


docs = load_pdfs()
chunks = split_text(docs)

print("Pages:", len(docs))
print("Chunks:", len(chunks))
print("First Chunk:")
print(chunks[0]["text"][:300])