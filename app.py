import streamlit as st
import pickle
import numpy as np

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="Smart Crop Recommendation",
    page_icon="🌱",
    layout="centered"
)

# ---------------- Load Model ----------------
model = pickle.load(open("model.pkl", "rb"))

# ---------------- Language ----------------
language = st.selectbox(
    "🌐 Select Language",
    ["English", "मराठी", "हिंदी"]
)

# ---------------- Title ----------------
if language == "English":
    st.title("🌱 Smart Crop Recommendation System")
    st.write("Enter Soil and Weather Details")

elif language == "मराठी":
    st.title("🌱 स्मार्ट पीक शिफारस प्रणाली")
    st.write("माती आणि हवामानाची माहिती भरा")

else:
    st.title("🌱 स्मार्ट फसल अनुशंसा प्रणाली")
    st.write("मिट्टी और मौसम की जानकारी दर्ज करें")

# ---------------- Inputs ----------------
N = st.number_input("Nitrogen (N)", min_value=0)
P = st.number_input("Phosphorus (P)", min_value=0)
K = st.number_input("Potassium (K)", min_value=0)

temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
ph = st.number_input("Soil pH")
rainfall = st.number_input("Rainfall (mm)")

# ---------------- Button ----------------
if language == "English":
    button = "🌾 Predict Crop"
elif language == "मराठी":
    button = "🌾 पीक सुचवा"
else:
    button = "🌾 फसल बताइए"

# ---------------- Prediction ----------------
if st.button(button):

    data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    prediction = model.predict(data)[0]

    st.markdown("---")

    # Crop Result
    if language == "English":
        st.success(f"🌾 Recommended Crop : {prediction}")

    elif language == "मराठी":
        st.success(f"🌾 शिफारस केलेले पीक : {prediction}")

    else:
        st.success(f"🌾 अनुशंसित फसल : {prediction}")

    # ---------------- Fertilizer ----------------
    st.subheader("🌿 Fertilizer Recommendation")

    fertilizer = "Balanced NPK Fertilizer"

    if prediction == "Rice":
        fertilizer = "Urea + DAP"

    elif prediction == "Maize":
        fertilizer = "NPK 20-20-20"

    elif prediction == "Cotton":
        fertilizer = "Potash + Urea"

    elif prediction == "Sugarcane":
        fertilizer = "Urea + Compost"

    elif prediction == "Wheat":
        fertilizer = "DAP + Urea"

    st.info(fertilizer)

    # ---------------- Soil Health ----------------
    st.subheader("🌱 Soil Health Score")

    score = 100

    if ph < 5.5 or ph > 8:
        score -= 20

    if rainfall < 50:
        score -= 10

    if humidity < 30:
        score -= 10

    st.metric("Score", f"{score}/100")

    # ---------------- Yield ----------------
    st.subheader("🌾 Estimated Yield")

    yield_prediction = round((N + P + K) / 3 * 0.12, 2)

    st.metric("Yield", f"{yield_prediction} Ton/Hectare")

    # ---------------- Profit ----------------
    st.subheader("💰 Estimated Profit")

    profit = int(yield_prediction * 25000)

    st.metric("Profit", f"₹ {profit}")

# ---------------- Sidebar ----------------
st.sidebar.title("About Project")

st.sidebar.write("""
🌱 Smart Crop Recommendation System

This project recommends the best crop using Machine Learning.

Features

✅ Crop Recommendation

✅ Fertilizer Recommendation

✅ Soil Health Score

✅ Yield Prediction

✅ Profit Prediction

Developed Using

• Python

• Machine Learning

• Streamlit
""")