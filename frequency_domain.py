import streamlit as st
import plotly.graph_objects as go
import numpy as np

def render():
    st.header("Frequency Analysis")
    
    if st.session_state.analyzer is None:
        st.warning("Please load data in the Data Loading tab first.")
        return
        
    analyzer = st.session_state.analyzer
    
    # Get frequency components
    frequencies, magnitude = analyzer.analyze_frequency_components()
    
    # Plot frequency spectrum
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=frequencies[:len(frequencies)//2],
        y=magnitude[:len(frequencies)//2],
        mode='lines',
        name='Frequency Spectrum'
    ))
    
    fig.update_layout(
        title="Frequency Spectrum",
        xaxis_title="Frequency (Hz)",
        yaxis_title="Magnitude",
        height=600
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Add frequency analysis options
    st.subheader("Analysis Options")
    
    if st.button("Find Dominant Frequencies"):
        # Find peaks in frequency spectrum
        peak_indices = np.argsort(magnitude[:len(frequencies)//2])[-5:]
        dominant_freqs = frequencies[peak_indices]
        
        st.write("Top 5 Dominant Frequencies:")
        for i, freq in enumerate(dominant_freqs, 1):
            st.metric(f"Frequency {i}", f"{abs(freq):.2f} Hz") 