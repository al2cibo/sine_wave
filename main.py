from wave_analyzer import WaveAnalyzer

def main():
    # Initialize the analyzer with your Excel file
    analyzer = WaveAnalyzer('example.xlsx')
    
    # Load the data
    analyzer.load_data(
        sheet_name='Sheet1',  # Adjust as needed
        time_column='Time',   # Adjust column names as per your Excel file
        amplitude_column='Amplitude'
    )
    
    # Visualize the original wave
    analyzer.plot_wave()
    
    # Analyze and visualize frequency components
    analyzer.plot_frequency_spectrum()

if __name__ == "__main__":
    main() 