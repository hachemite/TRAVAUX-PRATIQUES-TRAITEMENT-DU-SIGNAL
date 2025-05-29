import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

# Paramètres
f = 5
Fe = 50 #Frequence d'echantillonnage en Hz sans utilser les comparateurs
Te = 1/Fe #periode d'echantillonnage en s
T=1 #Duree de la signal en s
t = np.arange(0,T,Te) #Temps en s

# Signal analogique
signal_analogique = np.sin(2**np.pi*f*t)

t_fine = np.linspace(0, T, 1000) # Points de temps plus fins pour la courbe

signal_analogique_fine = np.sin(2**np.pi*f*t_fine)

# Affichage
plt.figure(figsize=(12, 5))
plt.stem(t_fine, signal_analogique_fine,label='Signal analogique continu',color='blue')
plt.stem(t,signal_analogique,basefmt=" ",linefmt='orange',markerfmt='o',label='Signal Echantionnage')
plt.title("Signal Analogique et Echantionnage ")
plt.grid(True)

plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.tight_layout()
plt.show()
