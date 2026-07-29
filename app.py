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
    "Upload potato leaf images",
    type=["jpg", "jpeg", "png"],
    accept_multiple_files=True
)

# Make predictions and display results
if uploaded_files:
    for i, uploaded_file in enumerate(uploaded_files):
        img = Image.open(uploaded_file)
        label, healthy_pct, blight_pct = predict(model, img)

        st.markdown(f"### Image {i+1}: {uploaded_file.name}")
        st.image(img, width=300)
        st.write(f"**Prediction:** {label}")
        st.progress(int(healthy_pct), text=f"Healthy: {healthy_pct:.1f}%")
        st.progress(int(blight_pct), text=f"Late Blight: {blight_pct:.1f}%")
        st.divider()
