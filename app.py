import streamlit as st
import numpy as np
import tensorflow as tf
from PIL import Image

# Configure the page
st.set_page_config(page_title="Potato Leaf Disease Classifier", page_icon="",
layout="centered")

st.title("🥔 Potato Leaf Classifier")
st.write("Upload a potato leaf image to check for Late Blight disease.")

# Load the saved model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("models/potato_blight_classifier.keras")
    return model

# Prediction function
# Confirmed class order: index 0 = Potato_Late_blight, index 1 = Potato_healthy
def predict(model, pil_image):
    img = pil_image.convert("RGB").resize((128, 128))
    arr = np.expand_dims(np.array(img, dtype=np.float32), axis=0)
    prob_healthy = float(model.predict(arr, verbose=0)[0][0])
    prob_blight = 1.0 - prob_healthy
    label = "Healthy" if prob_healthy >= 0.5 else "Late Blight"
    return label, prob_healthy * 100, prob_blight * 100

# Build the UI
model = load_model()
uploaded_files = st.file_uploader(
    "Upload potato leaf image(s)",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

if uploaded_files:
    results = []

    # Process all images first
    for uploaded_file in uploaded_files:
        try:
            img = Image.open(uploaded_file)
            label, healthy_pct, blight_pct = predict(model, img)
            results.append({
                "filename": uploaded_file.name,
                "image": img,
                "label": label,
                "healthy_pct": healthy_pct,
                "blight_pct": blight_pct
            })
        except Exception as e:
            st.error(f"Error processing {uploaded_file.name}: {e}")

    # Summary at the top
    if results:
        healthy_count = sum(1 for r in results if r["label"] == "Healthy")
        blight_count = len(results) - healthy_count

        st.markdown("### Summary")
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Images", len(results))
        col2.metric("Healthy", healthy_count)
        col3.metric("Late Blight", blight_count)
        st.divider()

        # Individual results as expandable cards
        for i, r in enumerate(results):
            with st.expander(f"📷 {r['filename']} — {r['label']}", expanded=(len(results) <= 3)):
                col_img, col_data = st.columns([1, 1.2])
                with col_img:
                    st.image(r["image"], use_container_width=True)
                with col_data:
                    st.write(f"**Prediction:** {r['label']}")
                    st.progress(min(int(r["healthy_pct"]), 100), text=f"Healthy: {r['healthy_pct']:.1f}%")
                    st.progress(min(int(r["blight_pct"]), 100), text=f"Late Blight: {r['blight_pct']:.1f}%")
