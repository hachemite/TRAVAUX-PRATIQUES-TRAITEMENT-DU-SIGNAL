import numpy as np
import matplotlib.pyplot as plt

N = 128      
Fe = 44    
fo = 3

t = np.arange(N)/Fe
x = np.sin(2*np.pi*fo*t)

# Affichage
plt.figure(figsize=(12, 5))
plt.plot(t, x)
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.title('Signal sinusoïdal')
plt.grid(True)

plt.tight_layout()
plt.show()

