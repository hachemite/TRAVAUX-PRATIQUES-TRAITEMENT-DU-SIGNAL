import librosa
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, freqz

# Load audio file
audio_file = "sample-1.wav"
signal_audio, sr = librosa.load(audio_file, sr=None)
time = np.linspace(0, len(signal_audio)/sr, len(signal_audio))

# Create high frequency noise
f_bruit = 1000
amplitude_bruit = 0.5
bruit_haute_frequence = amplitude_bruit * np.sin(2 * np.pi * f_bruit * time)

signal_bruite = signal_audio + bruit_haute_frequence

# Define low-pass filter    
cutoff_frequency = 1000
order = 4
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

# Apply filter
b, a = butter_lowpass(cutoff_frequency, sr, order)
signal_filter = filtfilt(b, a, signal_bruite)

# Create visualization
plt.figure(figsize=(15, 12))

# Plot 1: Time domain comparison of all signals
plt.subplot(2, 1, 1)
# For better visibility, let's display only a small segment
segment_length = 2000  # Number of samples to display
start_index = 10000  # Starting position for more interesting segments

end_index = min(start_index + segment_length, len(signal_audio))
segment_time = time[start_index:end_index]

plt.plot(segment_time, signal_audio[start_index:end_index], 'g-', label='Original Signal', alpha=0.8)
plt.plot(segment_time, signal_bruite[start_index:end_index], 'r-', label='Noisy Signal', alpha=0.6)
plt.plot(segment_time, signal_filter[start_index:end_index], 'b-', label='Filtered Signal', alpha=0.8)
plt.title('Audio Signal Comparison (Time Domain)')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# Plot 2: Frequency domain view of all signals
plt.subplot(2, 1, 2)
# Calculate and plot frequency spectra
def plot_spectrum(signal, sr, label, color, alpha=0.7):
    N = len(signal)
    freq = np.fft.rfftfreq(N, d=1/sr)
    spectrum = np.abs(np.fft.rfft(signal))/N
    plt.semilogx(freq, 20 * np.log10(spectrum + 1e-10), color=color, label=label, alpha=alpha)
    return freq, spectrum

plot_spectrum(signal_audio, sr, 'Original Signal', 'g')
plot_spectrum(signal_bruite, sr, 'Noisy Signal', 'r')
plot_spectrum(signal_filter, sr, 'Filtered Signal', 'b')

plt.title('Frequency Spectrum Comparison')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude (dB)')
plt.xlim(20, sr/2)  # Show from 20Hz to Nyquist frequency
plt.legend()
plt.grid(True)


plt.tight_layout();plt.show()

