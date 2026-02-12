# 🏠 House Price Prediction (Beginner ML Project)

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python\&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.30-orange?logo=streamlit\&logoColor=white)](https://streamlit.io/)
[![Dataset](https://img.shields.io/badge/Dataset-Kaggle-red?logo=kaggle\&logoColor=white)](https://www.kaggle.com/datasets/harishkumardatalab/housing-price-prediction)
[![License](https://img.shields.io/badge/License-MIT-green)](LICENSE)

---

## 📌 Project Overview

House Price Prediction is a **beginner-friendly machine learning project** that predicts house prices based on features like **area, bedrooms, bathrooms, stories**, and more.

This project covers the **end-to-end ML workflow**:
**Data Loading → Preprocessing → Feature Engineering → Modeling → Evaluation → Deployment**.

💻 **Live Demo (Streamlit App):** [Click Here](https://house-price-predictors.streamlit.app/)

---

## 🎯 Objective

To build a **regression model** that accurately predicts house prices using historical data, helping beginners understand practical ML implementation.

---

## 📊 Dataset

* **Source:** Kaggle
* **Link:** [Housing Price Prediction Dataset](https://www.kaggle.com/datasets/harishkumardatalab/housing-price-prediction)

### Features (Sample)

* Area
* Bedrooms
* Bathrooms
* Stories
* Main Road
* Guest Room
* Basement
* Hot Water Heating
* Air Conditioning
* Parking
* Preferred Area

### Target Variable

* Price

---

## 🛠️ Technologies Used

* Python
* NumPy & Pandas
* Matplotlib & Seaborn
* Scikit-learn
* Joblib
* Torch (optional)
* Streamlit

---

## 🧠 Machine Learning Algorithms

* **Linear Regression**
* **Random Forest Regressor** (optional)

---

## 🔄 Project Workflow

1. Import required libraries
2. Load & explore the dataset
3. Handle missing values
4. Perform exploratory data analysis (EDA)
5. Feature selection & scaling
6. Split data into training & testing sets
7. Train regression models
8. Evaluate models using **R², MAE, MSE**
9. Make predictions and visualize results

---

## 📈 Model Evaluation Metrics

| Metric                        | Description                                                           |
| ----------------------------- | --------------------------------------------------------------------- |
| **R² Score**                  | Measures how well the model explains the variance in the data         |
| **Mean Absolute Error (MAE)** | Average of absolute differences between predictions and actual values |
| **Mean Squared Error (MSE)**  | Penalizes larger errors in predictions                                |

---

## 📂 Project Structure

```
House-Price-Prediction/
│── data/
│   └── housing.csv
│── notebook/
│   └── house_price_prediction.ipynb
│── app.py          # Streamlit app
│── model.pkl       # Trained model
│── requirements.txt
│── README.md
```

---

## 🚀 How to Run

### Jupyter Notebook

```bash
git clone https://github.com/sumitkumar1233edeedad/-House-Price-Prediction-using-Machine-Learning.git
cd House-Price-Prediction
pip install -r requirements.txt
jupyter notebook
```

### Streamlit Web App

```bash
pip install streamlit
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🌐 Streamlit App Features

* User-friendly interface
* Normal working processes showing. 
* Input fields for house features
* Real-time prediction output

---

## 📌 Results

The model predicts house prices with **reasonable accuracy** for a beginner-level project.
Advanced techniques and feature engineering can further improve performance.

---

## 🌱 Future Improvements

* Enhance Streamlit UI
* Deploy app on **Streamlit Cloud**
* Include advanced regression models
* Hyperparameter tuning
* Input validation and error handling

---

## 👤 Author

**Vanshuu SÖHAL** more share 
[GitHub](https://github.com/sumitkumar1233edeedad)

---

## ⭐ Acknowledgments

* Kaggle for providing the dataset
* Open-source ML community for guidance and inspiration

---
