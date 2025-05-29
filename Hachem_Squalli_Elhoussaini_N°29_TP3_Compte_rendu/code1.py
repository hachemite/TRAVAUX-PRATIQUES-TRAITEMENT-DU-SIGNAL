import librosa
import matplotlib.pyplot as plt
import numpy as np

audio_file = "sample-1.wav"

# Load audio file
signal_audio, sr = librosa.load(audio_file, sr=None)
time = np.linspace(0, len(signal_audio)/sr, len(signal_audio))

# Create high frequency noise
f_bruit = 1000
amplitude_bruit = 0.5
bruit_haute_frequence = amplitude_bruit * np.sin(2 * np.pi * f_bruit * time)

# Create noisy signal
signal_bruite = signal_audio + bruit_haute_frequence

# Create figure
plt.figure(figsize=(14, 5))

# Plot both signals on the same graph
plt.plot(time, signal_audio, color="red", alpha=0.7, label='Signal original')
plt.plot(time, signal_bruite, color="blue", alpha=0.5, label='Signal bruité')

# Add title and labels
plt.title('Comparaison du signal audio original et du signal bruité')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()

# Adjust layout and show
plt.tight_layout()
plt.show()