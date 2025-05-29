import librosa
import numpy as np
import pygame
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



signal_bruit_int16 = np.int16(np.clip(signal_bruite, -1, 1) * 32767)
pygame.mixer.init(frequency=44100)
sound = pygame.mixer.Sound(buffer=signal_bruit_int16.tobytes())
sound.play()
while pygame.mixer.get_busy():
    pygame.time.Clock().tick(10)
    
    
output_file = "code2.wav"
sf.write(output_file, sound, sr)
print(f"bruit audio enrigistrer dans: {output_file}")
    
    