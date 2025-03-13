import streamlit as st

def show_header():
    """Display the application header"""
    st.markdown("""
    <div class="banner">
        <h1>Skin Cancer Detection</h1>
        <p class="subtitle">Upload a skin image to detect and classify potential skin cancer lesions</p>
    </div>
    """, unsafe_allow_html=True)