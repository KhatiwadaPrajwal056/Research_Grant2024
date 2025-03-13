import streamlit as st
from components.header import show_header
from components.image_upload import show_image_upload
from components.results import show_results
from components.about import show_about_section
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    
    st.set_page_config(page_title="Skin Cancer Detection", page_icon="🔬", layout="wide")
    
    # Load CSS
    with open("static/css/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    
    # Show header
    show_header()
    
    # Create two columns layout
    col1, col2 = st.columns([1, 1])
    
    # Show image upload in first column
    with col1:
        show_image_upload()
    
    # Show results in second column
    with col2:
        show_results()
    
    # Show about section
    show_about_section()

if __name__ == "__main__":
    main()