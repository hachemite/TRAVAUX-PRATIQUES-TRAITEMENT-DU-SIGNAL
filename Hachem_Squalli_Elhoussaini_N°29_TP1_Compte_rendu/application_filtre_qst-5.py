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
y2 = scipy.signal.lfilter(h,[1],x)

# Calcul des transformées de Fourier
X_f = np.fft.fft(x)    
H_f = np.fft.fft(h, N)   
Y1_f = np.fft.fft(y1)
Y2_f = np.fft.fft(y2)
f = np.fft.fftfreq(N, d=1/Fe) 

# Affichage
plt.figure(figsize=(12, 10))

# Module de X(f)
plt.subplot(2, 2, 1)
plt.plot(f, np.abs(X_f))
plt.title('Module de X(f)', pad=20)
plt.xlabel('Fréquence (Hz)')
plt.ylabel('|X(f)|')
plt.grid()

# Module de H(f)
plt.subplot(2, 2, 2)
plt.plot(f, np.abs(H_f))
plt.title('Module de H(f)', pad=20)
plt.xlabel('Fréquence (Hz)')
plt.ylabel('|H(f)|')
plt.grid()

# Module de Y1(f)
plt.subplot(2, 2, 3)
plt.plot(f, np.abs(Y1_f))
plt.title('Module de Y1(f)', pad=20)
plt.xlabel('Fréquence (Hz)')
plt.ylabel('|Y1(f)|')
plt.grid()

# Module de Y2(f)
plt.subplot(2, 2, 4)
plt.plot(f, np.abs(Y2_f))
plt.title('Module de Y2(f)', pad=20)
plt.xlabel('Fréquence (Hz)')
plt.ylabel('|Y2(f)|')
plt.grid()

plt.tight_layout()
plt.show()