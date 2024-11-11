import streamlit as st
import numpy as np
import pandas as pd
import plotly.graph_objects as go

def render():
    st.header("Statistical Analysis")
    
    if st.session_state.analyzer is None:
        st.warning("Please load data in the Data Loading tab first.")
        return
        
    analyzer = st.session_state.analyzer
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Basic Statistics")
        stats = {
            "Mean": np.mean(analyzer.amplitude),
            "Median": np.median(analyzer.amplitude),
            "Std Dev": np.std(analyzer.amplitude),
            "Variance": np.var(analyzer.amplitude),
            "Skewness": pd.Series(analyzer.amplitude).skew(),
            "Kurtosis": pd.Series(analyzer.amplitude).kurtosis()
        }
        
        for name, value in stats.items():
            st.metric(name, f"{value:.4f}")
            
    with col2:
        st.subheader("Distribution")
        fig = go.Figure()
        fig.add_trace(go.Histogram(
            x=analyzer.amplitude,
            nbinsx=50,
            name="Amplitude Distribution"
        ))
        
        fig.update_layout(
            title="Amplitude Distribution",
            xaxis_title="Amplitude",
            yaxis_title="Count",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True) 