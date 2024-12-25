import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import spectrogram

class LofarSimulator:
    def __init__(self, sampling_rate=1000, duration=10, noise_level=0.1, num_hydrophones=40):
        self.sampling_rate = sampling_rate  # Sampling rate in Hz
        self.duration = duration  # Duration of the signal in seconds
        self.noise_level = noise_level  # Noise level
        self.num_hydrophones = num_hydrophones  # Number of hydrophones in the array
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

    def generate_hydrophone_signals(self, frequencies, amplitudes, phases):
        """
        Generate signals for all hydrophones in the array.

        Args:
            frequencies: List of frequencies (Hz) for the signal.
            amplitudes: List of amplitudes for each frequency.
            phases: List of phase offsets (radians) for each frequency.

        Returns:
            A list of signals, one for each hydrophone.
        """
        return [
            self.generate_signal(frequencies, amplitudes, phases)
            for _ in range(self.num_hydrophones)
        ]

    def beamform(self, signals):
        """
        Simulate beamforming by summing signals from multiple hydrophones with delays.

        Args:
            signals: List of signals from different hydrophones.

        Returns:
            Beamformed signal.
        """
        # Introduce time delays for each hydrophone signal
        delays = np.linspace(0, 0.01, len(signals))  # Simulate small delays across hydrophones
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
        plt.ylim(0, 500)  # Focus on the low-frequency range of interest
        plt.show()

# Example usage
if __name__ == "__main__":
    simulator = LofarSimulator(sampling_rate=1000, duration=10, noise_level=0.1, num_hydrophones=40)

    # Generate multiple signals for the hydrophone array
    signals = simulator.generate_hydrophone_signals([10, 30, 60], [1, 0.8, 0.5], [0, np.pi / 4, np.pi / 6])

    # Perform beamforming
    beamformed_signal = simulator.beamform(signals)

    # Analyze the frequency of the beamformed signal
    frequencies, times, spec = simulator.analyze_frequency(beamformed_signal)

    # Plot the spectrogram
    simulator.plot_spectrogram(frequencies, times, spec)
