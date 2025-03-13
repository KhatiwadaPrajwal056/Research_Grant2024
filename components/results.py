import streamlit as st
import pandas as pd
import plotly.express as px

def show_results():
    """Display the analysis results"""
    st.markdown("### Analysis Results")
    
    if 'result' in st.session_state:
        result = st.session_state.result
        
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        
        if result.get("LesionDetected") is False:
            st.markdown(f"<h2>🟢 {result.get('PredictedClass')}</h2>", unsafe_allow_html=True)
            st.markdown(f"<p>Confidence: <strong>{result.get('Confidence')}%</strong></p>", unsafe_allow_html=True)
            st.markdown(f"""
            <div class="confidence-meter">
                <div class="confidence-value" style="width: {result.get('Confidence')}%;">
                    {result.get('Confidence')}%
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("<p>No further action is required based on this analysis, but please consult a healthcare professional if you have concerns.</p>", unsafe_allow_html=True)
            
        else:
            lesion_confidence = result.get('Confidence', 0)
            
            if result.get("MalignantPredicted") is True:
                malignant_confidence = result.get('confidence', 0)

                prediction_class = result.get("MalignantPredictedClass", "Malignant")
                st.markdown(f"<h2>🔴 {prediction_class}</h2>", unsafe_allow_html=True)
                st.markdown(f"<p>Lesion Detection Confidence: <strong>{lesion_confidence}%</strong></p>", unsafe_allow_html=True)
                st.markdown("<p><strong>Important:</strong> This analysis suggests a potential malignant lesion. Please consult a dermatologist as soon as possible.</p>", unsafe_allow_html=True)
                st.markdown(f"""
                <p>Malignant Detection Confidence: <strong>{malignant_confidence}%</strong></p>
                <div class="confidence-meter">
                    <div class="confidence-value" style="width: {malignant_confidence}%;">
                        {malignant_confidence}%
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                benign_confidence = result.get('confidence', 0)
                prediction_class = result.get("BenignPredictedClass", "Benign")
                st.markdown(f"<h2>🟡 {prediction_class}</h2>", unsafe_allow_html=True)
                st.markdown(f"<p>Lesion Detection Confidence: <strong>{lesion_confidence}%</strong></p>", unsafe_allow_html=True)
                st.markdown("<p>This analysis suggests a benign (non-cancerous) lesion. However, it's always recommended to consult a healthcare professional for a proper diagnosis.</p>", unsafe_allow_html=True)
                st.markdown(f"""
                <p>Benign Detection Confidence: <strong>{benign_confidence}%</strong></p>
                <div class="confidence-meter">
                    <div class="confidence-value" style="width: {benign_confidence}%;">
                        {benign_confidence}%
                    </div>
                </div>
                """, unsafe_allow_html=True)

            
            if "SubClassification" in result:
                st.markdown("#### Detailed Classification")
                
                sub_data = pd.DataFrame({
                    'Category': list(result["SubClassification"].keys()),
                    'Confidence': list(result["SubClassification"].values())
                })
                
                sub_data = sub_data.sort_values('Confidence', ascending=False)
                
                fig = px.bar(
                    sub_data, 
                    x='Category', 
                    y='Confidence', 
                    color='Confidence',
                    color_continuous_scale=['#e9ecef', '#4e54c8'],
                    text='Confidence',
                    labels={'Confidence': 'Confidence (%)', 'Category': 'Classification'},
                    height=300
                )
                
                fig.update_layout(
                    margin=dict(l=20, r=20, t=30, b=20),
                    paper_bgcolor='rgba(0,0,0,0)',
                    plot_bgcolor='rgba(0,0,0,0)',
                )
                
                fig.update_traces(texttemplate='%{text:.2f}%', textposition='inside')
                
                st.plotly_chart(fig, use_container_width=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
        
    else:
        st.markdown("""
        <div class="small-result-card" style="text-align: center; padding: 20px;">
            <img src="https://img.icons8.com/fluency/96/000000/upload-to-cloud.png" style="opacity: 0.5; width: 30px; height: 30px;">
            <p style="color: #666; margin-top: 10px; font-size: 12px;">Upload an image and click "Analyze Image" to see results here.</p>
        </div>
        """, unsafe_allow_html=True)
        
    st.markdown("""
    <div class="disclaimer">
        ⚠️ <strong>Medical Disclaimer:</strong> This tool is for informational purposes only and should not be considered medical advice.
        Always consult with a qualified healthcare provider.
    </div>
    """, unsafe_allow_html=True)