import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter
f = 5
Fe = 1000
Te = 1/Fe
t = np.arange(0,1,Te)
signal = np.sin(2**np.pi*f*t)

# Affichage
plt.figure(figsize=(12, 5))
plt.plot(t, signal)
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.title('Signal sinusoïdal')
plt.grid(True)

plt.tight_layout()
plt.show()
