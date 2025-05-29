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
# Différentes combinaisons de coefficients
coeffs = [(1.0, 0.5), (0.5, 1.0), (0.8, -0.8), (0.2, 0.2)]

plt.figure(figsize=(12, 8))
for i, (b0, b1) in enumerate(coeffs, 1):
    b = [b0, b1]
    h = lfilter(b, a, impulsion)
    
    plt.subplot(2, 2, i)
    plt.stem(h)
    plt.title(f'b0={b0}, b1={b1}')
    plt.xlabel('n')
    plt.ylabel('h(n)')
    plt.grid()

plt.tight_layout()
plt.show()