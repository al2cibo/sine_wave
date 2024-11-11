import streamlit as st
from wave_analyzer import WaveAnalyzer
from tabs import data_loader, time_domain, frequency_domain, statistics

def main():
    st.set_page_config(
        page_title="Wave Analysis Dashboard",
        page_icon="🌊",
        layout="wide"
    )
    
    st.title("Wave Analysis Dashboard")
    
    # Initialize session state for storing the analyzer
    if 'analyzer' not in st.session_state:
        st.session_state.analyzer = None
        
    # Create tabs
    tabs = st.tabs([
        "Data Loading",
        "Time Domain Analysis",
        "Frequency Analysis",
        "Statistics"
    ])
    
    # Render each tab
    with tabs[0]:
        data_loader.render()
        
    with tabs[1]:
        time_domain.render()
        
    with tabs[2]:
        frequency_domain.render()
        
    with tabs[3]:
        statistics.render()

if __name__ == "__main__":
    main() 