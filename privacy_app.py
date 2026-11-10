
import streamlit as st

st.set_page_config(
    page_title="PrivacyCheck",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 PrivacyCheck")

st.subheader("Personal Data Protection Tool")

st.write(
    "PrivacyCheck helps identify sensitive "
    "information before sharing text online."
)

st.info(
    "Enter text to check for possible privacy risks."
)
