import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import lfilter

b0, b1 = 0.8, 0.8
b = [b0, b1]
a = [1]  

impulsion = np.zeros(10)
impulsion[0] = 1  
h = lfilter(b, a, impulsion)

# Visualisation
plt.stem(h)
plt.title('Réponse impulsionnelle pour b0=b1=0.8')
plt.xlabel('n')
plt.ylabel('h(n)')
plt.grid()
plt.show()