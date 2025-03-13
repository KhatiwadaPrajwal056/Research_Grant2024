import streamlit as st

def show_about_section():
    """Display the about section"""
    st.markdown("### About Skin Cancer Detection")
    st.markdown("""
    <div class="result-card">
        <p><strong>Skin cancer</strong> is one of the most common types of cancer. Early detection significantly increases the chances of successful treatment. 
        This tool uses AI to analyze images of skin lesions and provide an initial assessment.</p> 

        🔍 Types of Skin Lesions
           - Benign: Non-cancerous growths like moles, seborrheic keratoses, and dermatofibromas.
           - Malignant: Cancerous growths including melanoma (mel), basal cell carcinoma (bcc), and squamous cell carcinoma.
       
        📸 How to Take Good Skin Images
           - Use good lighting — natural daylight works best.
           - Keep the camera steady to avoid blurriness.
           - Include a ruler or coin for scale.
           - Take multiple images from different angles.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="researchers-btn" onclick="this.nextElementSibling.style.display=this.nextElementSibling.style.display==\'none\'?\'block\':\'none\'">Researchers</div><div style="display:none;">', unsafe_allow_html=True)

    researchers_col1, researchers_col2, researchers_col3, researchers_col4 = st.columns(4)

    researchers = [
        ("Iza KC", "assets/iza.jpeg", "https://www.linkedin.com/in/izakc/"),
        ("Prajwal Khatiwada","assets/prajwal.jpg", "https://www.linkedin.com/in/prajwal-khatiwada-9481991b6/"),
        ("Samrat Adhikari", "assets/samrat.jpeg", "https://www.linkedin.com/in/samrat-kumar-adhikari/"),
        ("Er. Pralhad Chapagain", "assets/pralhad.jpeg", "https://www.linkedin.com/in/pralhad-chapagain-243332117/")
    ]

    for col, (name, img_path, linkedin_url) in zip(
        [researchers_col1, researchers_col2, researchers_col3, researchers_col4], researchers
    ):
        with col:
            st.markdown(f"<h5 style='text-align: center;'>{name}</h5>", unsafe_allow_html=True)
            st.image(img_path, use_container_width=False)
            st.markdown(f"""
            <div style="text-align: center;">
                <a href="{linkedin_url}" target="_blank">
                    <button class="linkedin-btn">LinkedIn</button>
                </a>
            </div>
            """, unsafe_allow_html=True)



