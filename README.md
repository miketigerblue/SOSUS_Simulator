# SOSUS Simulator

This repository contains a Python-based simulator inspired by the historical **Sound Surveillance System (SOSUS)**, a Cold War-era underwater monitoring network. The simulator is designed to replicate some of the core principles of SOSUS, including:

- Low-frequency acoustic signal generation
- Hydrophone array simulation
- Beamforming for signal detection and directionality
- Spectrogram visualisation (Lofargram simulation)

This project is linked to an article on my [portfolio site](#), which explores the historical context and technological advancements of SOSUS.

---

## Project Background

SOSUS was a classified U.S. Navy system developed in the 1950s to monitor Soviet submarine activity using the SOFAR (Sound Fixing and Ranging) channel. It utilised hydrophone arrays installed on the seabed to detect low-frequency acoustic signals over long distances. Declassified in 1992, SOSUS also contributed to oceanographic research in later years.

This simulator recreates some of the principles used in SOSUS:
- **Hydrophone Array**: Models a 40-node array, similar to the one deployed near the Bahamas in the 1950s.
- **Low-Frequency Signals**: Simulates submarine and vessel noise in the 10–500 Hz range, propagated through the SOFAR channel.
- **Beamforming**: Implements basic delay-and-sum beamforming for directional signal processing.
- **Spectrogram Visualisation**: Generates spectrograms (lofargrams) to analyze acoustic signal patterns over time.

---

## Features

1. **Hydrophone Array Simulation**: Creates a cluster of hydrophones with configurable parameters (e.g., number of nodes, spacing, delays).
2. **Submarine Signal Generation**: Simulates realistic low-frequency signals, including harmonics and amplitude modulation.
3. **Beamforming**: Processes hydrophone signals to isolate directional sound sources.
4. **Spectrogram Plotting**: Visualises the frequency content of the beamformed signal, mimicking a real lofargram.

---

## How to Run

1. Clone the repository:
```
git clone https://github.com/miketigerblue/SOSUS_Simulator.git
```
2. 
Install dependancies
```
pip install -r requirements.txt
```
3. 
Run the Simulation:
```
python lofar_sim.py
```

- **Hydrophone Array**

File Structure
- **lofar_sim.py**: Main Python file containing the simulator code.
- **README.md**: Documentation for the repository.
- **requirements.txt**: Dependencies for the project (e.g., NumPy, Matplotlib, SciPy).

## References

Wikipedia: SOSUS
SOFAR Channel Basics
Portfolio Article on SOSUS and the Simulator

## License

This project is licensed under the MIT License. See the LICENSE file for details.

