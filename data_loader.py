import streamlit as st
import pandas as pd
from wave_analyzer import WaveAnalyzer

def render():
    st.header("Data Loading")
    
    uploaded_file = st.file_uploader(
        "Upload Excel file containing wave data",
        type=['xlsx', 'xls']
    )
    
    if uploaded_file is not None:
        try:
            # Create analyzer instance
            analyzer = WaveAnalyzer(uploaded_file)
            
            # Show column selection
            df_preview = pd.read_excel(uploaded_file, nrows=5)
            columns = df_preview.columns.tolist()
            
            col1, col2 = st.columns(2)
            
            with col1:
                time_column = st.selectbox(
                    "Select Time Column",
                    options=columns,
                    index=0
                )
                
            with col2:
                amplitude_column = st.selectbox(
                    "Select Amplitude Column",
                    options=columns,
                    index=min(1, len(columns)-1)
                )
            
            if st.button("Load Data"):
                with st.spinner("Loading data..."):
                    analyzer.load_data(
                        time_column=time_column,
                        amplitude_column=amplitude_column
                    )
                    st.session_state.analyzer = analyzer
                    st.success("Data loaded successfully!")
                    
                    # Show data preview
                    st.subheader("Data Preview")
                    st.dataframe(analyzer.data.head())
                    
        except Exception as e:
            st.error(f"Error loading data: {str(e)}") 