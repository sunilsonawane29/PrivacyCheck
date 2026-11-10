
import streamlit as st


def display_privacy_score(score):
    """Display privacy risk score."""

    score = max(0, min(100, score))

    st.subheader("Privacy Risk Score")

    st.metric("Risk Score", f"{score}/100")

    st.progress(score / 100)

    if score <= 20:
        st.success("Low Privacy Risk")
    elif score <= 50:
        st.warning("Moderate Privacy Risk")
    elif score <= 75:
        st.warning("High Privacy Risk")
    else:
        st.error("Critical Privacy Risk")
