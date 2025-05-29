import numpy as np 
import scipy.signal
import matplotlib.pyplot as plt

N=128
fo=3
Fe=32
a=0.8

t= np.arange(N)/Fe


x = np.sin(2*np.pi*fo*t)




#application de filtre récursif
y1 = scipy.signal.lfilter([1],[1,-a],x)



#affichage
plt.figure(figsize=(10,5))
plt.plot(t,x,label="Signal original (sinusoide)",linestyle="--")
plt.plot(t,y1,label="Signal filtré",linewidth=2)

plt.title(f"Filtrage d'une sinusoide à 3 Hz par un filtre récursif (a=0.8)", pad=20)
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude ')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

