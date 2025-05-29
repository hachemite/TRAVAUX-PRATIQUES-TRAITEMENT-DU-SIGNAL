import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter 
from scipy.fft import fft, fftfreq

b0, b1 = 0.8, 0.8
b = [b0, b1]
a = [1]  


N_fft = 1024  
h_padded = np.zeros(N_fft)
h_padded[:2] = [b0, b1] 
H = fft(h_padded)
freqs = fftfreq(N_fft, d=1/44e3)  


# Visualisation du module
plt.figure()
plt.plot(freqs[:N_fft//2], np.abs(H[:N_fft//2]))
plt.title('Réponse fréquentielle du filtre')
plt.xlabel('Fréquence (Hz)')
plt.ylabel('|H(f)|')
plt.grid()
plt.show()
