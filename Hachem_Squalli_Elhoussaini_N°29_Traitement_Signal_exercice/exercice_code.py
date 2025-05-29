import numpy as np
import matplotlib.pyplot as plt

f1 = 5 
f2 = 50  
fe = 200 
Te = 1/fe  
duration = 2  
alpha = 0.9

n_samples = int(duration * fe)
n = np.arange(n_samples)
t = n * Te

signal = np.sin(2 * np.pi * f1 * t)
noise = np.sin(2 * np.pi * f2 * t)
x = signal + noise

y = np.zeros_like(x)
y[0] = (1 - alpha) * x[0] 
for i in range(1, len(x)):
    y[i] = (1 - alpha) * x[i] + alpha * y[i-1]


plt.figure(figsize=(10, 8))
#Signal d'entrée bruité
plt.subplot(2, 1, 1)
plt.plot(t, x, label='Signal bruité')
plt.plot(t, signal, 'g--', label='Signal original (5 Hz)')
plt.title('Signal d\'entrée bruité', pad=20)
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

# Signal filtré
plt.subplot(2, 1, 2)
plt.plot(t, y, 'g', label='Signal filtré')
plt.plot(t, signal, 'r--', label='Signal original (5 Hz)')
plt.title(f'Signal filtré (α={alpha})', pad=20)
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()# Commentaire sur l'effet du filtre
print("\nObservation:")
print(f"Le filtre avec alpha={alpha} reduit le bruit a 50 Hz et garde le signal a 5 Hz. Un alpha proche de 1 filtre plus mais peut creer du retard.")