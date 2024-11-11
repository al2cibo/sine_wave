import streamlit as st
import plotly.graph_objects as go
import numpy as np

def render():
    st.header("Time Domain Analysis")
    
    if st.session_state.analyzer is None:
        st.warning("Please load data in the Data Loading tab first.")
        return
        
    analyzer = st.session_state.analyzer
    
    # Time domain plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=analyzer.time,
        y=analyzer.amplitude,
        mode='lines',
        name='Wave'
    ))
    
    fig.update_layout(
        title="Wave Form",
        xaxis_title="Time",
        yaxis_title="Amplitude",
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Add analysis options
    st.subheader("Analysis Options")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("Calculate Peak-to-Peak"):
            p2p = np.ptp(analyzer.amplitude)
            st.metric("Peak-to-Peak Amplitude", f"{p2p:.2f}")
            
    with col2:
        if st.button("Calculate RMS"):
            rms = np.sqrt(np.mean(analyzer.amplitude**2))
            st.metric("RMS Value", f"{rms:.2f}") 