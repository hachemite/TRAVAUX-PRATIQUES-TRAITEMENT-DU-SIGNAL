import numpy as np 
import scipy.signal
import matplotlib.pyplot as plt

#------------------etude temporel------------------------
N=20

dirac = np.zeros(N)
dirac[0] = 1

b=[1] #numerator


for i in [0.8,-0.8,0.99,1.01]:
    a = i

    den = [1,-a]#denominator

    h =  scipy.signal.lfilter(b,den,dirac)

    plt.stem(range(N),h)


    plt.title(f"Reponse impultsionnel du filtere (a={i})", pad=20)
    plt.xlabel('n')
    plt.ylabel('j(n)')
    plt.grid(True)
    plt.show()

