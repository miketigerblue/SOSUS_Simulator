import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

class LofarSimulator:
    def __init__(self, sampling_rate=1000, duration=10, noise_level=0.1):
        self.sampling_rate = sampling_rate  # Sampling rate in Hz
        self.duration = duration  # Duration of the signal in seconds
        self.noise_level = noise_level  # Noise level
        self.time = np.linspace(0, duration, int(sampling_rate * duration))  # Time axis

    def generate_signal(self, frequencies, amplitudes, phases):
        """
        Generate a synthetic signal based on multiple frequency components.

        Args:
            frequencies: List of frequencies (Hz) to include in the signal.
            amplitudes: List of amplitudes for each frequency.
            phases: List of phase offsets (radians) for each frequency.

        Returns:
            A numpy array containing the generated signal.
        """
        signal = np.zeros_like(self.time)
        for f, a, p in zip(frequencies, amplitudes, phases):
            signal += a * np.sin(2 * np.pi * f * self.time + p)
        # Add noise to the signal
        signal += self.noise_level * np.random.normal(size=len(self.time))
        return signal

    def beamform(self, signals):
        """
        Simulate beamforming by summing signals from multiple arrays with delays.

        Args:
            signals: List of signals from different arrays.

        Returns:
            Beamformed signal.
        """
        # Introduce time delays for each signal
        delays = np.linspace(0, 0.01, len(signals))  # Simulate small delays
        beamformed_signal = np.zeros_like(signals[0])
        for signal, delay in zip(signals, delays):
            delay_samples = int(delay * self.sampling_rate)
            beamformed_signal += np.roll(signal, delay_samples)
        return beamformed_signal

    def analyze_frequency(self, signal):
        """
        Perform frequency analysis using a spectrogram.

        Args:
            signal: The input signal to analyze.

        Returns:
            Frequencies, times, and the spectrogram matrix.
        """
        frequencies, times, spec = spectrogram(
            signal, self.sampling_rate, nperseg=256, noverlap=128
        )
        return frequencies, times, spec

    def plot_spectrogram(self, frequencies, times, spec):
        """
        Plot the spectrogram of the signal.

        Args:
            frequencies: Frequency axis of the spectrogram.
            times: Time axis of the spectrogram.
            spec: Spectrogram matrix.
        """
        plt.figure(figsize=(10, 6))
        plt.pcolormesh(times, frequencies, 10 * np.log10(spec), shading='gouraud')
        plt.title('Spectrogram (Lofargram Simulation)')
        plt.xlabel('Time (s)')
        plt.ylabel('Frequency (Hz)')
        plt.colorbar(label='Intensity (dB)')
        plt.show()

# Example usage
if __name__ == "__main__":
    simulator = LofarSimulator()

    # Generate multiple signals to simulate an array
    signals = [
        simulator.generate_signal([50, 120], [1, 0.5], [0, np.pi / 4]),
        simulator.generate_signal([50, 120], [1, 0.5], [np.pi / 8, np.pi / 3]),
        simulator.generate_signal([50, 120], [1, 0.5], [np.pi / 4, np.pi / 6]),
    ]

    # Perform beamforming
    beamformed_signal = simulator.beamform(signals)

    # Analyze the frequency of the beamformed signal
    frequencies, times, spec = simulator.analyze_frequency(beamformed_signal)

    # Plot the spectrogram
    simulator.plot_spectrogram(frequencies, times, spec)