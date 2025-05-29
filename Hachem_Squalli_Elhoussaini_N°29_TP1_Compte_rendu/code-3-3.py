#Filtrage par convulution (en utilisatn lfilter comme FTR avec h)
import numpy as np 
import scipy.signal
import matplotlib.pyplot as plt

a = 0.8
N=20



N=128
fo=3
Fe=32
a=0.8
L=50
t= np.arange(N)/Fe

h = a**np.arange(L)



x = np.sin(2*np.pi*fo*t)




#application de filtre récursif
y1 = scipy.signal.lfilter([1],[1,-a],x)



y2= scipy.signal.lfilter(h,[1],x)

#affichage des resultat

#affichage
plt.figure(figsize=(12,6))

plt.subplot(3,1,1)
plt.plot(t,y1,label=" filtrage recursig",linewidth=2)
plt.title(f"Filtrage y1", pad=20)
plt.xlabel('Temps (s)')
plt.ylabel('Amplitude ')
plt.legend()
plt.grid(True)


plt.subplot(3,1,2)
plt.plot(t,y2[:N],"--",label=" y2 :convulution avec h",linewidth=2)
plt.title(f"Filtrage y2", pad=20)
plt.legend()
plt.grid(True)


plt.subplot(3,1,3)
plt.plot(np.arange(L),h)
plt.title(f"Résponse impulsionnelle h(n)", pad=20)
plt.grid(True)

plt.tight_layout()
plt.show()



