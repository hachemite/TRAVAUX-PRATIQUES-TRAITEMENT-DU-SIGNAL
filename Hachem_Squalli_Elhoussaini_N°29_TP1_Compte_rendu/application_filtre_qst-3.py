import numpy as np
import matplotlib.pyplot as plt
import scipy

N = 128      
Fe = 44    

b0, b1 = 0.8, 0.8
b = [b0, b1]
a = [1] 
t = np.arange(N)/Fe
x = np.sin(2*np.pi*3*t)
h = np.array([b0, b1])  

y2= scipy.signal.lfilter(h,[1],x)

#affichage
plt.figure(figsize=(10,5))
plt.plot(t,x,label="Signal original (sinusoide)",linestyle="--")
plt.plot(t,y2,label="Signal filtré",linewidth=2)

plt.title(f"Filtrage d'une sinusoide à 3 Hz par un filtre récursif (b0=b1=0.8)", pad=20)
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()