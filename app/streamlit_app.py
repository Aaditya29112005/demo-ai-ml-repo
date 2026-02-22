import streamlit as st
import requests

st.set_page_config(page_title="Vehicle AI Maintenance", layout="wide")

st.title("🚀 Advanced Vehicle Maintenance Prediction")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.header("Vehicle Parameters")
    mileage = st.slider("Mileage (km)", 0, 200000, 50000)
    age = st.number_input("Vehicle Age (Years)", 0, 20, 5)
    issues = st.number_input("Reported Issues", 0, 10, 0)
    
    if st.button("Predict Maintenance Risk"):
        # Call API
        # response = requests.post("http://localhost:8000/predict", json={...})
        risk = (issues * 10) + (mileage / 10000)
        st.metric("Maintenance Risk Score", f"{risk:.2f}%")
        if risk > 50:
            st.error("High Risk: Maintenance Recommended")
        else:
            st.success("Low Risk: Vehicle is Stable")

with col2:
    st.header("AI Maintenance Assistant")
    user_input = st.text_input("Ask me anything about your vehicle...")
    if user_input:
        st.chat_message("user").write(user_input)
        st.chat_message("assistant").write(f"Based on your vehicle state, {user_input} is a valid concern. I recommend checking the brake pads given your mileage.")

st.markdown("---")
st.info("This is a multi-domain AI system mockup for the Advanced Roadmap.")
