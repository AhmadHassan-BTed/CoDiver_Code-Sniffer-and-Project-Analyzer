import streamlit as st
import pandas as pd

def render_summary_metrics(df: pd.DataFrame, total_kloc: float, cocomo: dict):
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric("Total Files", len(df))
        st.metric("Total kLOC", round(total_kloc, 2))

    with col2:
        st.metric("Avg Cyclomatic Complexity", round(df['cyclomatic_complexity'].mean(), 2))
        st.metric("Avg Cognitive Complexity", round(df['cognitive_complexity'].mean(), 2))

    with col3:
        st.metric("Total Function Points", round(df['function_points'].sum(), 2))
        st.metric("Avg Defect Density", round(df['defect_density'].mean(), 4))

    with col4:
        st.metric("Estimated Effort (person-months)", cocomo['effort'])
        st.metric("Estimated Duration (months)", cocomo['time'])
        st.metric("Estimated Team Size (persons)", cocomo['staff'])

def render_recommendations(df: pd.DataFrame, threshold: int):
    st.subheader("💡 Refactoring Recommendations")
    complex_files = df[df['cyclomatic_complexity'] > threshold]
    if not complex_files.empty:
        for _, row in complex_files.iterrows():
            st.warning(
                f"**File '{row['filename']}'** has high complexity "
                f"(Cyclomatic: {row['cyclomatic_complexity']}, "
                f"Cognitive: {row['cognitive_complexity']}). "
                "Consider breaking down into smaller, more modular functions."
            )
    else:
        st.success("All files are within the complexity threshold!")
