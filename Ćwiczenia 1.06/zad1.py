import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import matplotlib.ticker as mtick

fun = lambda x: np.log(x)
num = 1000
granice_calkowania = (1, 10)


class CalkaProstokatna:
    a, b, n = 0, 0, 1
    calka = 0
    f = 0

    def __init__(self, granice, n, f):
        # a,b - Granice całkowania. Całka jest od a do b
        if not granice:
            self.a = 0
            self.b = 1
        else:
            self.a = granice[0]
            self.b = granice[1]

        # Tutaj ustalamy ilość węzłów po drodze
        if not n:
            self.n = 100
        else:
            self.n = n

        # Tu ustalamy jaką funkcję całkujemy
        self.f = f

        # Tutaj wykonuje się sama procedura policzenia całki
        self.licz()

    def licz(self):
        # Teraz policzymy przyrost dx jaki chcemy brać
        dx = (self.b - self.a) / self.n
        # Tutaj robimy numpyArray do liczenia
        punkty = (np.linspace(self.a, self.b, num=self.n))
        # Teraz mapujemy pola prostokątów na kolejne elementy listy
        wartosci = list(map(self.f, punkty))
        # Suma wartosci daje nam całkę metodą prostokątów
        self.calka = dx * sum(wartosci)

    def __repr__(self):
        return f"Wartość całki metodą prostokątów z sqrt(x) od {self.a} do {self.b} to: {self.calka}"

    def __add__(self, other):
        if type(other) == type(self):
            return self.calka + other.calka
        else:
            return self.calka + other

    __radd__ = __add__

    def __mul__(self, other):
        if type(other) == type(self):
            return self.calka * other.calka
        else:
            return self.calka * other

    __rmul__ = __mul__


class CalkaTrapez:
    a, b, n = 0, 0, 1
    calka = 0
    f = 0

    def __init__(self, granice, n, f):
        # a,b - Granice całkowania. Całka jest od a do b
        if not granice:
            self.a = 0
            self.b = 1
        else:
            self.a = granice[0]
            self.b = granice[1]

        # Tutaj ustalamy ilość węzłów po drodze
        if not n:
            self.n = 100
        else:
            self.n = n

        # Tu ustalamy jaką funkcję całkujemy
        self.f = f

        # Tutaj wykonuje się sama procedura policzenia całki
        self.licz()

    def licz(self):
        # Teraz policzymy przyrost dx jaki chcemy brać
        dx = (self.b - self.a) / self.n
        # Tutaj robimy numpyArray do liczenia
        punkty = (np.linspace(self.a, self.b, num=self.n))
        # Teraz mapujemy pola prostokątów na kolejne elementy listy
        wartosci = list(map(self.f, punkty))
        # Suma wartosci daje nam całkę metodą prostokątów
        wart_posrednie = []
        for l in range(len(wartosci)-1):
            a = wartosci[l]
            b = wartosci[l+1]
            wart_posrednie.append((a+b)*dx/2)
        self.calka = sum(wart_posrednie)

    def __repr__(self):
        return f"Wartość całki metodą trapezów z sqrt(x) od {self.a} do {self.b} to: {self.calka}"

    def __add__(self, other):
        if type(other) == type(self):
            return self.calka + other.calka
        else:
            return self.calka + other

    __radd__ = __add__

    def __mul__(self, other):
        if type(other) == type(self):
            return self.calka * other.calka
        else:
            return self.calka * other

    __rmul__ = __mul__


class CalkaSimpsona:
    a, b, n = 0, 0, 1
    calka = 0
    f = 0

    def __init__(self, granice, n, f):
        # a,b - Granice całkowania. Całka jest od a do b
        if not granice:
            self.a = 0
            self.b = 1
        else:
            self.a = granice[0]
            self.b = granice[1]

        # Tutaj ustalamy ilość węzłów po drodze
        if not n:
            self.n = 100
        else:
            self.n = n

        # Tu ustalamy jaką funkcję całkujemy
        self.f = f

        # Tutaj wykonuje się sama procedura policzenia całki
        self.licz()

    def licz(self):
        # Teraz policzymy przyrost dx jaki chcemy brać
        dx = (self.b - self.a) / self.n
        # Tutaj robimy numpyArray do liczenia
        punkty = (np.linspace(self.a, self.b, num=self.n))
        punkty_srod = (np.linspace(self.a+dx/2, self.b-dx/2, num=self.n))
        # Teraz mapujemy pola prostokątów na kolejne elementy listy
        wartosci = list(map(self.f, punkty))
        # Suma wartosci daje nam całkę metodą prostokątów
        wart_srodkowe = list(map(self.f, punkty_srod))
        wart_posrednie = []
        for l in range(len(wartosci) - 1):
            a = wartosci[l]
            b = wartosci[l + 1]
            c = wart_srodkowe.pop()
            pole = (lambda x, y, z: x + y + 4*z)(a, b, c)
            wart_posrednie.append(pole)
        self.calka = dx/6 * sum(wart_posrednie)

    def __repr__(self):
        return f"Wartość całki metodą simpsona z sqrt(x) od {self.a} do {self.b} to: {self.calka}"

    def __add__(self, other):
        if type(other) == type(self):
            return self.calka + other.calka
        else:
            return self.calka + other

    __radd__ = __add__

    def __mul__(self, other):
        if type(other) == type(self):
            return self.calka * other.calka
        else:
            return self.calka * other

    __rmul__ = __mul__


def porownanie(funkcja, granice_calk):
    lp = 2
    lk = 100
    wynik = integrate.quad(fun, granice_calkowania[0], granice_calkowania[1])

    p1 = list(map(lambda n: CalkaProstokatna(granice_calk,  n, funkcja).calka, [i for i in range(lp, lk)]))
    t1 = list(map(lambda n: CalkaTrapez(granice_calk,  n, funkcja).calka, [i for i in range(lp, lk)]))
    s1 = list(map(lambda n: CalkaSimpsona(granice_calk, n, funkcja).calka, [i for i in range(lp, lk)]))
    fig, ax = plt.subplots()
    plt.title("Wyliczona wartość w funkcji ilości węzłów")
    ax.scatter([i for i in range(lp, lk)], p1, label='Prostokąt', s=5)
    ax.scatter([i for i in range(lp, lk)], t1, label='Trapez', s=5)
    ax.scatter([i for i in range(lp, lk)], s1, label='Simpson', s=5)
    ax.hlines(y=wynik[0], xmin=0, xmax=lk, label='Wartość rzeczywista', color='magenta')
    ax.legend()
    fig.show()
    plt.show()


def porownanie2(funkcja, granice_calk):
    lp = 2
    lk = 100
    wynik = integrate.quad(fun, granice_calkowania[0], granice_calkowania[1])

    p1 = list(map(lambda n: (CalkaProstokatna(granice_calk, n, funkcja).calka-wynik[0])/wynik[0], [i for i in range(lp, lk)]))
    t1 = list(map(lambda n: (CalkaTrapez(granice_calk, n, funkcja).calka-wynik[0])/wynik[0], [i for i in range(lp, lk)]))
    s1 = list(map(lambda n: (CalkaSimpsona(granice_calk, n, funkcja).calka-wynik[0])/wynik[0], [i for i in range(lp, lk)]))

    fig, ax = plt.subplots()
    plt.title("Procentowe odchylenie od wartości rzeczywistej w funkcji ilości węzłów")
    ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))
    ax.scatter([i for i in range(lp, lk)], p1, label='Prostokąt', s=5)
    ax.scatter([i for i in range(lp, lk)], t1, label='Trapez', s=5)
    ax.scatter([i for i in range(lp, lk)], s1, label='Simpson', s=5)
    ax.legend()
    fig.show()
    plt.show()


porownanie(fun, granice_calkowania)
porownanie2(fun, granice_calkowania)

print(CalkaProstokatna(granice_calkowania, num, fun))
print(CalkaTrapez(granice_calkowania, num, fun))
print(CalkaSimpsona(granice_calkowania, num, fun))
print(f"Wartość rzeczywista to {integrate.quad(fun, granice_calkowania[0], granice_calkowania[1])[0]}")
