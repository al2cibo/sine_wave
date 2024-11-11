import pandas as pd
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from typing import Tuple, List

class WaveAnalyzer:
    def __init__(self, file_path: str):
        """Initialize the wave analyzer with the Excel file path."""
        self.file_path = file_path
        self.data = None
        self.sampling_rate = None
        
    def load_data(self, sheet_name: str = 'Sheet1', 
                  time_column: str = 'Time',
                  amplitude_column: str = 'Amplitude') -> None:
        """Load and validate data from Excel file."""
        try:
            self.data = pd.read_excel(self.file_path, sheet_name=sheet_name)
            self._validate_columns([time_column, amplitude_column])
            self.time = self.data[time_column].values
            self.amplitude = self.data[amplitude_column].values
            self._calculate_sampling_rate()
        except Exception as e:
            raise Exception(f"Error loading data: {str(e)}")
            
    def _validate_columns(self, required_columns: List[str]) -> None:
        """Validate that required columns exist in the dataset."""
        missing_columns = [col for col in required_columns if col not in self.data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
            
    def _calculate_sampling_rate(self) -> None:
        """Calculate the sampling rate from time data."""
        time_diff = np.diff(self.time)
        self.sampling_rate = 1 / np.mean(time_diff)
        
    def analyze_frequency_components(self) -> Tuple[np.ndarray, np.ndarray]:
        """Perform FFT analysis on the wave."""
        if self.data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
            
        frequencies = np.fft.fftfreq(len(self.amplitude), 1/self.sampling_rate)
        fft_result = np.fft.fft(self.amplitude)
        return frequencies, np.abs(fft_result)
    
    def plot_wave(self) -> None:
        """Plot the original wave."""
        plt.figure(figsize=(12, 6))
        plt.plot(self.time, self.amplitude)
        plt.title('Wave Form')
        plt.xlabel('Time')
        plt.ylabel('Amplitude')
        plt.grid(True)
        plt.show()
        
    def plot_frequency_spectrum(self) -> None:
        """Plot the frequency spectrum."""
        frequencies, magnitude = self.analyze_frequency_components()
        
        plt.figure(figsize=(12, 6))
        plt.plot(frequencies[:len(frequencies)//2], 
                magnitude[:len(frequencies)//2])
        plt.title('Frequency Spectrum')
        plt.xlabel('Frequency (Hz)')
        plt.ylabel('Magnitude')
        plt.grid(True)
        plt.show() 