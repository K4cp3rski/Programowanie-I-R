import time
import math

# Wysyłamy na mail gonz@fuw.edu.pl

start = time.process_time()

lista = []
prime_list = []
prime = 0

dl = int(input("Jaka jest długość listy? \n"))
print("Wpisz po kolei szukane liczby")
for i in range(0, dl):
    # print("Kolejna liczba to: ")
    lista.append(int(input()))
print(f"Wprowadzone liczby to: {lista}")


def sito(n):
    primes = []
    for nr in range(2, n+1):
        primes.append(nr)
    # print(primes)
    lb = 2
    while lb <= int(math.sqrt(n)):
        # Jeśli liczbę lb widzimy w tablicy primes, to usuwamy jej wszystkie wielokrotności aż do sqrt(naszej liczby)
        if lb in primes:
            # zmienna rm, będzie nam oznaczać wieloktorności naszej liczby, które to będziemy usuwać z tablicy.
            for rm in range(lb*2, n+1, lb):
                if rm in primes:
                    primes.remove(rm)
        lb = lb + 1
    # print(primes)
    return primes


for g in range(0, dl):
    num = lista[g]
    if num in sito(num):
        prime_list.append(num)
if not prime_list:
    print("Nie wprowadzono liczb pierwszych")
else:
    print(prime_list)

# print(sito(19))
duration = time.process_time() - start
print("{0:02f}s".format(duration))
