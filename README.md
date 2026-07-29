# 🥔 CV4 Potato Late Blight Classifier

GET 324 (AI & Machine Learning) Mini-Project — Laboratory Exercise 10
**Task:** Binary image classification — Healthy Potato vs Potato Late Blight

## Live App
https://cv4-potato-late-blight-classifier-b3fecbtgnhmvk6rgbckdl9.streamlit.app
> **Note:** This app is hosted on Streamlit Community Cloud's free tier, which puts apps to sleep after a period of inactivity. If the link shows a "Zzzz... this app has gone to sleep" screen, simply click **"Yes, get this app back up!"** and wait 30–60 seconds for it to restart.

## About
This application classifies potato leaf images as Healthy or affected by Late Blight, using a MobileNetV3 transfer-learning model trained on the PlantVillage dataset (Kaggle, via kagglehub). The model achieved 100% test accuracy and F1-score on a held-out test set of 95 images. Users upload a leaf photo through the web interface and receive an instant prediction with confidence percentages. Key challenges included managing Colab session timeouts during dataset preparation, and a Streamlit Cloud deployment failure caused by a Python-version mismatch with TensorFlow's available wheels — resolved by pinning the Python version via a `.python-version` file. Future improvements could include adding the Early Blight class for three-way classification, and expanding the test set for more robust evaluation.

## How to Use
1. Open the live app link above
2. Upload a photo of a potato leaf (JPG or PNG)
3. View the prediction and confidence scores for Healthy vs Late Blight

## Group Members (CV4)
| Name | Registration Number | GitHub Username |
|------|---------------------|------------------|
| Imetom Emmanuel Iniobong | 23/EG/CV/061 | Robot-Mark5 |
| Johnson Success Innocent | 23/EG/CV/001 | Success-1404 |
| Nnitor Emmanuel Emmanuel | 23/EG/CV/011 | Nnitor001 |
| Adah Covenant Victor | 23/EG/CV/081 | covenantpaul |
| Udoise Miracle Stephen | 23/EG/CV/031 | Miraboy7 |
| Uduak Uduakabasi Johnson | 23/EG/CV/021 | Yhudee10 |
| Emeh Godspower Okon | 23/EG/CV/071 | Godspower-6 |

## Contributors' Notes
- **Imetom Emmanuel Iniobong:** Model training, deployment, and Streamlit troubleshooting
- **Johnson Success Innocent:** Dataset research and preparation  
- **Nnitor Emmanuel Emmanuel:** Testing the deployed app
- **Emeh Godspower Okon:** Documentation and report writing
- **Uduak Uduakabasi Johnson:** Model training and evaluation support 
- **Udoise Miracle Stephen:** Reviewed and proofread README
- **[Member 7]:**
- 
## Tech Stack
- TensorFlow / Keras (MobileNetV3Small transfer learning)
- Streamlit (web interface)
- Google Colab (training environment)
- GitHub + Streamlit Community Cloud (version control & deployment)
