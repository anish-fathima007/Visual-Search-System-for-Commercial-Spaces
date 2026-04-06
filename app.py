import streamlit as st
from feature_extractor import extract_features
from similarity import find_similar
from PIL import Image
import os

st.title("Visual Search for Commercial Spaces")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image")

    # Save temp
    temp_path = "temp.jpg"
    image.save(temp_path)

    # Extract features
    query_emb = extract_features(temp_path)

    # Find similar
    results = find_similar(query_emb, "dataset/embeddings.pkl")

    st.subheader("Top Matches")

    for img_name, score in results:
        img_path = os.path.join("dataset/images", img_name)
        st.image(img_path, caption=f"{img_name} | Score: {score:.3f}")