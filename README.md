# TFG
# 🎓 **Phenomenological Multivariate Analysis of Mental Health Issues using AI on Voice Data**

> 👩‍🎓 *Grado en Ingeniería en Tecnologías de Telecomunicación*  
> 📍 *Universidad Pontificia Comillas (ICAI)*  
> 🧠 Mental Health · 🎤 Voice Biomarkers · 🤖 Machine Learning · 📊 Multivariate Analysis  

---

## 📌 Project Overview

This repository contains the full implementation of my final degree project, which explores the use of **AI** and **voice analysis** to identify psychological conditions such as **anxiety** and **depression**. By leveraging real-time emotion, tone, and speech analysis from user-generated content (TikTok, YouTube, etc.), this project contributes to building a **cost-effective**, **scalable**, and **non-invasive** mental health diagnostic platform.

> 🧭 The methodology is built around **StressTech API**, advanced **ML models**, and structured **data pipelines**.

---

## 🧠 Motivation

The social and economic impact of untreated mental health issues is staggering. Depression and anxiety alone cause over **$1 trillion/year** in lost productivity. This project aims to provide a **low-cost**, **scalable**, and **automated** solution to address this global challenge, especially in the workplace.

---

## 🎯 Objectives

1. **🧪 Develop a Multivariate Diagnostic Tool for Organizations**
2. **🎯 Improve Precision and Accessibility of Diagnostics**
3. **🛠 Enable Proactive Interventions in Companies**
4. **💸 Reduce Direct and Indirect Costs**
5. **📚 Contribute to AI-Driven Mental Health Research**

---

## 🗂️ Repository Structure

### 📁 **Main Directory**
| File | Description |
|------|-------------|
| `API_uploading.py` | Uploads video files to the StressTech API via presigned URLs. |
| `output_API_download.py` | Downloads analysis results from the API and saves them in `.json` format. |
| `json_generator.py` | Aggregates all result files into a structured dataset for ML. |
| `newurls.py` | Generates filenames and result URLs from the initial CSV. |
| `TextTranslation.py` | Adds original speech and translation data into the final CSV. |
| `urls.txt` / `urls_tiktok.txt` | Input URL lists used for downloading videos. |
| `tiktok_downloading.bat` / `video_downloading.bat` | Automated scripts to fetch video content. |
| `README.md` | Full documentation of the project (this file). |

---

### 📁 `my-ypnbs/` – 🔬 **Model Notebooks**

| Notebook | Description |
|----------|-------------|
| `DEF_RegressionLogisticaBinaria.ipynb` | Binary classification using Logistic Regression. |
| `DEF_SVM.ipynb` | Support Vector Machine with tuned kernels for emotion classification. |
| `DEF_HGB.ipynb` | Gradient Boosting model for robust multi-class predictions. |
| `DEF_RandomForest.ipynb` | Ensemble model to interpret importance of vocal features. |
| `DEF_RedesNeuronales.ipynb` | Feedforward neural network for deep learning analysis. |
| `DEF_MultiRegresion.ipynb` | Regression analysis for continuous psychological traits. |

---

## 🔄 Pipeline Summary

The following summarizes the end-to-end workflow of the project:

1. **📥 Video Collection**  
   Short-form videos are collected from platforms like TikTok and YouTube using `urls.txt` and `.bat` automation scripts.

2. **☁️ Video Upload to API**  
   Videos are uploaded to the StressTech API using `API_uploading.py`, which returns presigned `upload_url` and `result_url` for each video.

3. **📤 Downloading Analysis Results**  
   After processing, JSON results are downloaded using `output_API_download.py` and saved to the `resultados/` directory.

4. **🔗 URL Generation**  
   The script `newurls.py` parses and formats filenames and result endpoints from a base CSV, creating a mapping for later integration.

5. **📊 Dataset Construction**  
   The JSON files are parsed using `json_generator.py`, extracting biometric, emotional, and textual indicators into a structured CSV.

6. **🗣 Text + Translation Enrichment**  
   With `TextTranslation.py`, each row in the dataset is enriched with detected speech and its translation.

7. **🤖 Model Training & Evaluation**  
   Machine learning models (SVM, Random Forest, Neural Networks, etc.) are trained using the `.ipynb` notebooks in the `my-ypnbs/` folder.

8. **📈 Visualization and Insights**  
   Outputs are interpreted using confusion matrices, ROC curves, and feature importance plots to assess model performance.

9. **🧠 Interpretation for Mental Health Diagnosis**  
   The final models are evaluated based on their ability to identify emotional states (e.g., stress, depression, anxiety) from voice/text patterns.
