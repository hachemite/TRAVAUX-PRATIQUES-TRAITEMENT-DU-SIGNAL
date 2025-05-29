import numpy as np 
import scipy.signal
import matplotlib.pyplot as plt


fe = 32
Te = 1/fe  
a_values = [-0.8,0.8]
N=512

plt.figure(figsize=(10,5))
for a in a_values:
    #impulsion de dirac
    dirac = np.zeros(N)
    dirac[0] =1
    
    #Réponse impulsionnellle h(n)
    b =[1]
    den = [1,-a]#denominator
    h =  scipy.signal.lfilter(b,den,dirac)

    #Transformee de fourir 
    H =np.fft.fft(h)
    H = np.abs(H[:N//2]) #module + demi spectre (fréquence réelle)
    f =np.linspace(0,0.5,N//2) #axe des fréquences

    
    plt.plot(f,H,label=f'a={a}')



plt.title(f"Module de la réponse fréquentielll H=(f) )", pad=20)
plt.xlabel('Frequence')
plt.ylabel('H(f)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()




