import numpy as np
from matplotlib import pyplot as plt
def calka_trapez(f, przedzial, n):
    podzial = np.linspace(przedzial[1],przedzial[0], n+1)
    wysokosc = (przedzial[1]-przedzial[0])/(n)
    suma = 0
    for  index, i in enumerate(podzial[:-1]):
        suma += (f(i)+f(podzial[index+1]))*wysokosc/2
    #print(suma)
    return suma

def calka_simpsona(f, przedzial, n):
    a = przedzial[0]
    b = przedzial[1]
    wysokosc = (b-a)/n
    podzial_1 = np.linspace(a, b, n+1)
    podzial_2 = np.linspace(a+wysokosc/2, b-wysokosc/2, n)
    suma_wezly = sum(f(np.linspace(a+wysokosc, b-wysokosc, n-2)))
    suma_srodki = sum(f(podzial_2))
    suma = (b-a)/(6*n)*(f(a)+f(b)+2*suma_wezly+4*suma_srodki)
    #print(suma)
    return suma

def f(x):
    return np.log(x)
calka_trapez(f,(0,1),10)
calka_simpsona(f,(0,1),10)
def porownanie(f, granice):
    trapez = list(map(lambda n: calka_trapez(f, granice, n), [i for i in range(2,50)]))
    simpson = list(map(lambda n: calka_simpsona(f, granice, n), [i for i in range(2,50)]))
    fig, ax = plt.subplots()
    ax.scatter([i for i in range(2,50)], trapez, label = 'trapex')
    ax.scatter([i for i in range(2,50)], simpson, label = 'simpson')
    ax.legend()
    fig.show()
    plt.show()
porownanie(f, (1,10))
