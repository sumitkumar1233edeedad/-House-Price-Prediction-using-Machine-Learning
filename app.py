import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Page config
st.set_page_config(page_title="🏡 House Price Predictor", layout="centered")

# Title
st.title("🏡 House Price Prediction System")
st.markdown("Predict a house price using **Machine Learning** 💡")

# Sidebar for input (optional) or columns
with st.expander("🏠 Enter House Details"):
    col1, col2 = st.columns(2)

    with col1:
        area = st.slider('📐 Area (sq ft)', 1650, 16200, 10000, step=100)
        bedrooms = st.slider('🛏️ Bedrooms', 1, 6, 2)
        bathrooms = st.slider('🛁 Bathrooms', 1, 6, 2)
        stories = st.radio('🏢 Stories', [1, 2, 3, 4])

    with col2:
        mainroad = 1 if st.selectbox('🛣️ On Main Road?', ['Yes', 'No']) == 'Yes' else 0
        guestroom = 1 if st.selectbox('🛋️ Guest Room Available?', ['Yes', 'No']) == 'Yes' else 0
        basement = 1 if st.selectbox('🏚️ Basement Available?', ['Yes', 'No']) == 'Yes' else 0
        hotwaterheating = 1 if st.selectbox('🔥 Hot Water Heating?', ['Yes', 'No']) == 'Yes' else 0
        airconditioning = 1 if st.selectbox('❄️ Air Conditioning?', ['Yes', 'No']) == 'Yes' else 0
        parking = st.radio('🚗 Parking Slots', [0, 1, 2, 3])
        prefarea = 1 if st.selectbox('⭐ Preferred Area?', ['Yes', 'No']) == 'Yes' else 0

# Load model and scaler
scaler = joblib.load("scaled.pkl")
model = joblib.load("model.pkl")

# Prediction
if st.button("💰 Predict Price"):
    input_data = np.array([[area, bedrooms, bathrooms, stories,
                            mainroad, guestroom, basement,
                            hotwaterheating, airconditioning,
                            parking, prefarea]])

    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    prediction = np.expm1(prediction) * 1000

    st.balloons()
    st.metric(label="🏷️ Predicted House Price", value=f"${prediction[0]:,.2f}")

    # Feature Importance
    st.subheader("📊 Feature Importance")
    features = ['area', 'bedrooms', 'bathrooms', 'stories',
                'mainroad', 'guestroom', 'basement',
                'hotwaterheating', 'airconditioning',
                'parking', 'prefarea']
    importances = model.feature_importances_

    # Plotting with Seaborn
    fig, ax = plt.subplots(figsize=(8, 5))
    sns.barplot(x=importances, y=features, palette="viridis", ax=ax)
    ax.set_title("Feature Importance", fontsize=14)
    ax.set_xlabel("Importance Score")
    ax.set_ylabel("Features")
    st.pyplot(fig)

st.markdown("---")

# Footer with columns and icons
col1, col2, col3 = st.columns([1,2,1])

with col1:
    st.markdown("💡 **Built with Streamlit & ML**")

with col2:
    st.markdown("<h4 style='text-align:center; color:#4B0082;'>🏡 House Price Predictor</h4>", unsafe_allow_html=True)

with col3:
    st.markdown("👨‍💻 **Project by [Vanshuu]()**", unsafe_allow_html=True)

# Optional: Add a thank you note or social links
st.markdown("<p style='text-align:center; color:gray;'>✨ Thanks for visiting! Follow me for more ML projects 🚀</p>", unsafe_allow_html=True)
