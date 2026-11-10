
import streamlit as st


def display_scan_results(results):
    """Display detected sensitive information."""

    st.subheader("Privacy Scan Results")

    if not results:
        st.success("No sensitive information detected.")
        return

    for category, items in results.items():
        st.write(f"### {category.capitalize()}")

        if items:
            st.warning(f"{len(items)} item(s) detected")

            for item in items:
                st.write("- Sensitive information detected")
        else:
            st.success("No issues detected")


def display_masked_text(masked_text):
    """Display text after masking sensitive data."""

    st.subheader("Protected Text")
    st.code(masked_text)
