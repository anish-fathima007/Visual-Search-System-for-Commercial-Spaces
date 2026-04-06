import os
import pickle
from feature_extractor import extract_features

def build_embeddings(image_folder, output_file):
    embeddings = {}

    for img_name in os.listdir(image_folder):
        path = os.path.join(image_folder, img_name)

        try:
            emb = extract_features(path)
            embeddings[img_name] = emb
            print(f"Processed: {img_name}")
        except Exception as e:
            print(f"Skipping {img_name}: {e}")

    with open(output_file, "wb") as f:
        pickle.dump(embeddings, f)

    print("Embeddings saved successfully!")