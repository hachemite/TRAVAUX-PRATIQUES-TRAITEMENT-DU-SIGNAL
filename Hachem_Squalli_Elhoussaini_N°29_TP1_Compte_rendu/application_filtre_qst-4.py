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

y1 = scipy.signal.lfilter(b,a,x)
y2= scipy.signal.lfilter(h,[1],x)


#affichage
plt.figure(figsize=(12, 6))
plt.plot(t, x, 'g', label='Entrée x(n)')
plt.plot(t, y1, 'b', label='y1 (lfilter)')
plt.plot(t, y2, 'r--', label='y2 (convolution)')
plt.title('Comparaison des méthodes de filtrage')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid()
plt.show()

# Différence entre les deux méthodes
plt.figure()
plt.plot(t, y1-y2)
plt.title('Différence entre y1 et y2')
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude')
plt.grid()
plt.show()