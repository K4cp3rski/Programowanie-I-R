import time
import math


start = time.process_time()

list = []
dl = int(input("Jaka jest długość listy? \n"))
print("Wpisz po kolei liczby")
for i in range(0, dl):
    # print("Kolejna liczba to: ")
    list.append(int(input()))
# print(f"{list}")


def srednia(list):
    n = len(list)
    licznik = 0
    for i in range(0,n):
        licznik = licznik + list[i]
    return float(licznik/n)


def wariancja(list):
    n = len(list)
    X = srednia(list)
    licznik = 0
    for i in range(0,n):
        licznik  = licznik + (list[i] - X)**2
    return float(licznik/n)

def odchylenie(list):
    return math.sqrt(wariancja(list))

def funkcje(list):
    return (srednia(list), wariancja(list),odchylenie(list))

print(f"Średnia to: {funkcje(list)[0]}")
print(f"Wariancja to: {funkcje(list)[1]}")
print(f"Odchylenie Standardowe to: {funkcje(list)[2]}")

duration = time.process_time() - start
print("{0:02f}s".format(duration))