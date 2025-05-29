import numpy as np 
import scipy.signal
import matplotlib.pyplot as plt

N=128
fo=3
Fe=32

t= np.arange(N)/Fe


x = np.sin(2*np.pi*fo*t)

    
plt.plot(x)


plt.title(f"Module de la réponse fréquentielll H=(f) )", pad=20)
plt.xlabel('Frequence')
plt.ylabel('H(f)')
plt.grid(True)
plt.tight_layout()
plt.show()


