import numpy as np
from embedding import model

def retrieve(query,index,chunks,k=3):
    query_embedding = model.encode([query])
    query_embedding = np.array(query_embedding,dtype="float32")
    distance,indices = index.search(query_embedding,k)

    results = []
    for idx in indices[0]:
        #Indices 0 because we are only searching for one query at a time
        #Appending chunks because we want to return the actual text of the chunks, not just their indices
        results.append(chunks[idx])
    return results