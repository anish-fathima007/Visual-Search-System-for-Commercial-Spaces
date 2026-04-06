import numpy as np
import pickle

def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def find_similar(query_embedding, embeddings_file, top_n=5):
    with open(embeddings_file, "rb") as f:
        data = pickle.load(f)

    scores = []

    for img_name, emb in data.items():
        score = cosine_similarity(query_embedding, emb)
        scores.append((img_name, score))

    # Sort by highest similarity
    scores.sort(key=lambda x: x[1], reverse=True)

    return scores[:top_n]