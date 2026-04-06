from feature_extractor import extract_features
from similarity import find_similar

# 👉 Change this to one of your actual image names
query_image = "dataset/images/office1.jpg"

# Extract features for query image
query_emb = extract_features(query_image)

# Find similar images
results = find_similar(query_emb, "dataset/embeddings.pkl")

print("\nTop Matches:\n")

# Print results
for name, score in results:
    print(f"{name} ---> Similarity: {score:.4f}")