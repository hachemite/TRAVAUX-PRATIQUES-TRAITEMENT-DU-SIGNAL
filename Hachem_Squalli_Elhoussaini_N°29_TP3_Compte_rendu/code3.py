import librosa
import numpy as np
import pygame
from scipy.signal import butter,filtfilt
import soundfile as sf  # enrigistrer WAV files
audio_file = "sample-1.wav"
sound = audio_file
# Load audio file
signal_audio, sr = librosa.load(audio_file, sr=None)
time = np.linspace(0, len(signal_audio)/sr, len(signal_audio))
# Create high frequency noise
f_bruit = 1000
amplitude_bruit = 0.5
bruit_haute_frequence = amplitude_bruit * np.sin(2 * np.pi * f_bruit * time)
# Create noisy signal
signal_bruite = signal_audio + bruit_haute_frequence

cuttoff_frequency = 500 
order = 4
def butter_lowpass(cutoff, fs, order=5):
    nyq = 0.5 * fs
    normal_cutoff = cutoff / nyq
    from scipy.signal import butter
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a
b,a = butter_lowpass(cuttoff_frequency,sr, order) 
signal_filter = filtfilt(b,a,signal_bruite) #filtre du signal bruité

signal_filter_int16 = np.int16(np.clip(signal_filter, -1, 1) * 32767)
pygame.mixer.init(frequency=sr)
sound = pygame.mixer.Sound(buffer=signal_filter_int16.tobytes())
sound.play()
while pygame.mixer.get_busy():
    pygame.time.Clock().tick(10)  
    
    
output_file = "code3.wav"
sf.write(output_file, sound, sr)
print(f"filtre audio enrigistrer dans : {output_file}")

    