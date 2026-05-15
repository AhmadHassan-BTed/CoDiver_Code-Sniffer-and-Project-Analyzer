import streamlit as st
import sys
from pathlib import Path
import pandas as pd
import json
from datetime import datetime

# Add paths to sys.path to resolve internal modules
ROOT_DIR = Path(__file__).parent
sys.path.append(str(ROOT_DIR / "src"))
sys.path.append(str(ROOT_DIR / "src" / "java_analyzer"))

# Global Page Configuration
st.set_page_config(
    page_title="Omniscient Quality Suite",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for unified dashboard
st.markdown("""
    <style>
    .main-header {
        font-size: 2.8rem;
        font-weight: 800;
        background: linear-gradient(120deg, #1e3a8a 0%, #3b82f6 100%, #10b981 200%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        color: #64748b;
        font-size: 1.2rem;
        margin-bottom: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Import Java dependencies
from java_analyzer.dashboard import (
    initialize_session_state,
    handle_analysis as handle_java_analysis,
    display_analysis_results as display_java_results,
    render_file_info as render_java_file_info
)

# Import Python/Agile dependencies
from software_metrics.calculators.code_analyzer import analyze_python_file
from software_metrics.calculators.estimation import calculate_cocomo
from software_metrics.calculators.agile import analyze_agile_metrics
from software_metrics.ui.components.metrics_cards import render_summary_metrics, render_recommendations
from software_metrics.ui.components.charts import (
    render_loc_distribution, 
    render_complexity_scatter, 
    render_quality_bar,
    render_agile_charts
)

# Initialize Java session state
initialize_session_state()

def render_unified_landing():
    st.markdown('<h1 class="main-header">🛡️ Omniscient Software Intelligence Suite</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Unified Code Quality, Architecture Metrics & Agile Process Analytics</p>', unsafe_allow_html=True)
    
    st.markdown("### 🎯 Unified Capabilities")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("#### ☕ Enterprise Java Analysis")
        st.markdown("- Deep AST Code Smell Detection\n- Design & Implementation Flaws\n- Maintainability Index")
    with col2:
        st.markdown("#### 🐍 Python Metrics")
        st.markdown("- Cyclomatic & Cognitive Complexity\n- Defect Density Prediction\n- COCOMO Estimation")
    with col3:
        st.markdown("#### 🏃 Agile Process")
        st.markdown("- Velocity Tracking\n- Scope Creep Analysis\n- Sprint Burndown")
    
    st.markdown("---")
    st.markdown("### 🔍 How to Use")
    st.markdown("""
    1. **Upload Files:** Use the Control Center sidebar to upload any combination of Python files, Java files, or Agile JSON data.
    2. **Configure Engines:** Adjust thresholds and toggle specific analyzers to tailor the strictness.
    3. **Execute:** Click the "Execute Omniscient Analysis" button to process all uploaded artifacts simultaneously.
    4. **Review Results:** Navigate through the dynamically generated tabs to explore unified insights seamlessly.
    """)
    st.info("👆 Awaiting data... Upload files from the Control Center to begin.")

def render_python_results(python_files, show_recommendations, complexity_threshold):
    metrics_data = []
    total_kloc = 0

    for uploaded_file in python_files:
        try:
            uploaded_file.seek(0)
            content = uploaded_file.read().decode('utf-8')
            metrics = analyze_python_file(content)
            if metrics:
                metrics_dict = {
                    'filename': uploaded_file.name,
                    'lines_of_code': metrics.lines_of_code,
                    'functions': metrics.functions,
                    'classes': metrics.classes,
                    'cyclomatic_complexity': metrics.cyclomatic_complexity,
                    'cognitive_complexity': metrics.cognitive_complexity,
                    'function_points': metrics.function_points,
                    'defect_density': metrics.defect_density
                }
                metrics_data.append(metrics_dict)
                total_kloc += metrics.lines_of_code / 1000
        except Exception as e:
            st.error(f"Error reading {uploaded_file.name}: {str(e)}")

    if metrics_data:
        df = pd.DataFrame(metrics_data)
        cocomo = calculate_cocomo(total_kloc)

        render_summary_metrics(df, total_kloc, cocomo)

        st.markdown("---")
        st.subheader("🔍 Detailed Code Metrics")
        ptabs = st.tabs(["📝 Code Metrics", "🧠 Complexity Analysis", "📉 Quality Indicators"])

        with ptabs[0]:
            st.dataframe(df, use_container_width=True)
            render_loc_distribution(df)

        with ptabs[1]:
            render_complexity_scatter(df)
            if show_recommendations:
                render_recommendations(df, complexity_threshold)

        with ptabs[2]:
            render_quality_bar(df, total_kloc)

def render_agile_results(sprint_data):
    try:
        sprint_data.seek(0)
        sprint_json = json.load(sprint_data)
        sprint_df = pd.DataFrame(sprint_json)

        if not sprint_df.empty:
            agile_metrics = analyze_agile_metrics(sprint_df)

            col1, col2 = st.columns(2)
            with col1:
                st.metric("Average Velocity", agile_metrics.get('average_velocity', 0))
            with col2:
                st.metric("Scope Creep", f"{agile_metrics.get('scope_creep_percentage', 0)}%")

            render_agile_charts(sprint_df)
    except Exception as e:
        st.error(f"Error analyzing agile data: {str(e)}")

def main():
    with st.sidebar:
        st.markdown("## 📂 Universal Control Center")
        
        st.markdown("### Source Code")
        python_files = st.file_uploader("Upload Python Files", type=['py'], accept_multiple_files=True)
        java_file = st.file_uploader("Upload Java Source File", type=["java"])
        
        st.markdown("### Process Data")
        sprint_data = st.file_uploader("Upload Sprint Data (JSON)", type=['json'])
        defect_data = st.file_uploader("Upload Defect Data (JSON)", type=['json'])
        
        st.markdown("---")
        st.markdown("### ⚙️ Engine Configuration")
        
        with st.expander("🐍 Python Analysis Settings", expanded=True):
            show_recommendations = st.checkbox("Show Refactoring Recommendations", value=True)
            complexity_threshold = st.slider("Complexity Warning Threshold", 5, 20, 10)
            
        with st.expander("☕ Java Analysis Settings", expanded=True):
            enable_design = st.checkbox("Design Smells", value=True)
            enable_implementation = st.checkbox("Implementation Smells", value=True)
            enable_naming = st.checkbox("Naming Conventions", value=True)
            enable_documentation = st.checkbox("Documentation", value=True)
            
        st.markdown("---")
        analyze_btn = st.button("🚀 Execute Omniscient Analysis", type="primary", use_container_width=True)
        
        st.caption("🔧 Unified Platform v4.0")
        st.caption(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Handle execute state
    if analyze_btn:
        st.session_state.omni_analyzed = True

    # Handle Java File Session State
    if java_file:
        java_file.seek(0)
        source_code = java_file.getvalue().decode("utf-8")
        if st.session_state.file_name != java_file.name:
            st.session_state.file_name = java_file.name
            st.session_state.source_code = source_code
            st.session_state.analysis_results = None
            st.session_state.analysis_metrics = None
            # Reset omni_analyzed if new file uploaded
            st.session_state.omni_analyzed = False

    has_content = bool(python_files or java_file or sprint_data)

    if not has_content:
        render_unified_landing()
    else:
        st.markdown('<h1 class="main-header">📊 Unified Analysis Results</h1>', unsafe_allow_html=True)
        
        tab_names = []
        if python_files: tab_names.append("🐍 Python Metrics")
        if java_file: tab_names.append("☕ Java Static Analysis")
        if sprint_data: tab_names.append("🏃 Agile Analytics")
        
        if not tab_names:
            return
            
        tabs = st.tabs(tab_names)
        tab_idx = 0
        
        if python_files:
            with tabs[tab_idx]:
                if st.session_state.get('omni_analyzed', False):
                    render_python_results(python_files, show_recommendations, complexity_threshold)
                else:
                    st.info("Click 'Execute Omniscient Analysis' in the sidebar to process the Python files.")
            tab_idx += 1
            
        if java_file:
            with tabs[tab_idx]:
                render_java_file_info(java_file.name, len(st.session_state.source_code), len(st.session_state.source_code.split('\n')))
                if analyze_btn:
                    handle_java_analysis(st.session_state.source_code)
                
                if st.session_state.analysis_results is not None:
                    display_java_results()
                elif not st.session_state.get('omni_analyzed', False):
                    st.info("Click 'Execute Omniscient Analysis' in the sidebar to run the Java AST Engine.")
            tab_idx += 1
            
        if sprint_data:
            with tabs[tab_idx]:
                if st.session_state.get('omni_analyzed', False):
                    render_agile_results(sprint_data)
                else:
                    st.info("Click 'Execute Omniscient Analysis' in the sidebar to process Agile Data.")
            tab_idx += 1

if __name__ == "__main__":
    main()
