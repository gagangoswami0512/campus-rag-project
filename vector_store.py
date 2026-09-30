import faiss
import numpy as np

def build_index(vectors):
    dimension = vectors.shape[1]

    index = faiss.IndexFlatL2(dimension)
    index.add(np.array(vectors, dtype="float32"))

    return index