# 🥔 CV4 Potato Late Blight Classifier

GET 324 (AI & Machine Learning) Mini-Project — Laboratory Exercise 10
**Task:** Binary image classification — Healthy Potato vs Potato Late Blight

## Live App
https://cv4-potato-late-blight-classifier-b3fecbtgnhmvk6rgbckdl9.streamlit.app

## About
This application classifies potato leaf images as Healthy or affected by Late Blight, using a MobileNetV3 transfer-learning model trained on the PlantVillage dataset (Kaggle, via kagglehub). The model achieved 100% test accuracy and F1-score on a held-out test set of 95 images. Users upload a leaf photo through the web interface and receive an instant prediction with confidence percentages. Key challenges included managing Colab session timeouts during dataset preparation, and a Streamlit Cloud deployment failure caused by a Python-version mismatch with TensorFlow's available wheels — resolved by pinning the Python version via a `.python-version` file. Future improvements could include adding the Early Blight class for three-way classification, and expanding the test set for more robust evaluation.

## How to Use
1. Open the live app link above
2. Upload a photo of a potato leaf (JPG or PNG)
3. View the prediction and confidence scores for Healthy vs Late Blight

## Group Members (CV4)
| Name | Registration Number | GitHub Username |
|------|---------------------|------------------|
| [Your Name] | [Reg Number] | [GitHub username] |
| [Member 2] | [Reg Number] | [GitHub username] |
| [Member 3] | [Reg Number] | [GitHub username] |
| [Member 4] | [Reg Number] | [GitHub username] |

## Tech Stack
- TensorFlow / Keras (MobileNetV3Small transfer learning)
- Streamlit (web interface)
- Google Colab (training environment)
- GitHub + Streamlit Community Cloud (version control & deployment)
