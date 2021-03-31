import time
import math


start = time.process_time()

n = int(input("Proszę wpisać liczbę, której rozkład ma być podany: \n"))

pierwsze = []

# Liczb pierwszych szukamy za pomocą metody sita arystotenesa

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

for i in sito(n):
    if n%i == 0:
        pierwsze.append(i)
print(pierwsze)

duration = time.process_time() - start
print("{0:02f}s".format(duration))