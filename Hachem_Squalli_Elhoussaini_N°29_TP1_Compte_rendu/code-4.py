import numpy as np
import matplotlib.pyplot as plt

N = 128      
Fe = 32       

# Création d'un signal x 
t = np.arange(N)/Fe
x = np.sin(2*np.pi*3*t)

# Création de la réponse impulsionnelle h 
a = 0.8
h = a ** np.arange(N)

# Calcul des transformées de Fourier
X_f = np.fft.fft(x)    
H_f = np.fft.fft(h)   
f = np.fft.fftfreq(N, d=1/Fe) 

# Affichage
plt.figure(figsize=(12, 5))

# Module de X(f)
plt.subplot(1, 2, 1)
plt.plot(f, np.abs(X_f))
plt.title('Module de X(f)')
plt.xlabel('Fréquence (Hz)')
plt.ylabel('|X(f)|')
plt.grid()

# Module de H(f)
plt.subplot(1, 2, 2)
plt.plot(f, np.abs(H_f))
plt.title('Module de H(f)')
plt.xlabel('Fréquence (Hz)')
plt.ylabel('|H(f)|')
plt.grid()

plt.tight_layout()
plt.show()