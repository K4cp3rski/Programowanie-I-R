import numpy as np

eps = (1e-14, 1e-14)
x0 = -1
n = 64
funkcja = lambda f: np.sin(f ** 2 - f + 1 / 3.0) + 0.5 * f


class Steffensen:
    wynik = 0
    result = False
    # # Parametry początkowe

    # Funkcja której pierwiastka szukamy
    fun = 0

    def __init__(self, funkcja, eps, x0, n):
        self.epsx = eps[0]  # Dokładność wyznaczania pierwiastka
        self.epsy = eps[1]  # Dokładność wyznaczania zera
        self.x = x0  # Punkt startowy
        self.n = n  # Maksymalna liczba obiegów
        self.fun = funkcja
        self.przyblizenie()

    def przyblizenie(self):

        # Program do przybliżenia
        while self.n > 0:
            h = self.fun(self.x)

            if abs(h) < self.epsy:
                self.result = True
                break
            g = (self.fun(self.x + h) - h) / h

            x1 = self.x

            self.x -= h / g

            if abs(x1 - self.x) < self.epsx:
                result = True
                break
            self.n -= self.n

    def __repr__(self):
        if self.result:
            return "Błąd!"
        else:
            return f"Znalezione przybliżenie pierwiastka to {self.x}"


print(Steffensen(funkcja, eps, x0, n))
