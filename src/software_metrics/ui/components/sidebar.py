import streamlit as st

def render_sidebar():
    with st.sidebar:
        st.header("📥 Project Data Input")
        python_files = st.file_uploader("Upload Python Files", type=['py'], accept_multiple_files=True)
        sprint_data = st.file_uploader("Upload Sprint Data (JSON)", type=['json'])
        defect_data = st.file_uploader("Upload Defect Data (JSON)", type=['json'])

        st.header("⚙️ Analysis Settings")
        show_recommendations = st.checkbox("Show Refactoring Recommendations", value=True)
        complexity_threshold = st.slider("Complexity Warning Threshold", 5, 20, 10)
        
        st.info("Upload your Python source files to see the analysis.")
        
    return python_files, sprint_data, defect_data, show_recommendations, complexity_threshold
