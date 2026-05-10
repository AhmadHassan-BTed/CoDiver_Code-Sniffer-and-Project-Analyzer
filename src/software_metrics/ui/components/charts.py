import streamlit as st
import plotly.express as px
import pandas as pd

def render_loc_distribution(df: pd.DataFrame):
    fig = px.histogram(df, x='lines_of_code',
                       title='Lines of Code Distribution',
                       labels={'lines_of_code': 'Lines of Code'},
                       color_discrete_sequence=['#636EFA'])
    st.plotly_chart(fig, use_container_width=True)

def render_complexity_scatter(df: pd.DataFrame):
    fig = px.scatter(df,
                    x='cyclomatic_complexity',
                    y='cognitive_complexity',
                    size='lines_of_code',
                    hover_data=['filename'],
                    title='Cyclomatic vs Cognitive Complexity',
                    color='cyclomatic_complexity',
                    color_continuous_scale='Viridis')
    st.plotly_chart(fig, use_container_width=True)

def render_quality_bar(df: pd.DataFrame, total_kloc: float):
    quality_metrics = pd.DataFrame({
        'Metric': ['Defect Density', 'Function Points per kLOC'],
        'Value': [
            df['defect_density'].mean(),
            df['function_points'].sum() / total_kloc if total_kloc > 0 else 0
        ]
    })
    fig = px.bar(quality_metrics, x='Metric', y='Value',
                 title='Quality Indicators',
                 color='Metric',
                 color_discrete_sequence=['#EF553B', '#00CC96'])
    st.plotly_chart(fig, use_container_width=True)

def render_agile_charts(sprint_df: pd.DataFrame):
    if 'completed_points' in sprint_df.columns:
        fig_velocity = px.line(sprint_df, x=sprint_df.index, y='completed_points',
                             title='Sprint Velocity Trend',
                             markers=True)
        st.plotly_chart(fig_velocity, use_container_width=True)

    if all(col in sprint_df.columns for col in ['remaining_points', 'sprint_day']):
        fig_burndown = px.line(sprint_df, x='sprint_day', y='remaining_points',
                             title='Sprint Burndown Chart',
                             markers=True)
        st.plotly_chart(fig_burndown, use_container_width=True)
