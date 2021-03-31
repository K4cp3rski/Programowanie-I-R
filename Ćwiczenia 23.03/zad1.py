import time


start = time.process_time()

slownik = {}
slownik['Masło'] = 2.3
slownik['Mleko'] = 1.5
slownik['Chleb'] = 5.2
slownik['Jajka'] = 3.0
slownik['Bulki'] = 0.3
slownik['Banany'] = 2.3
slownik['Jablka'] = 1.4
slownik['Zioło'] = 30.5
slownik['Kasztelan'] = 2.3
slownik['Ksiazece'] = 4.5

# Suma elementów
s = sum(slownik.values())
print(s)

# Średnia
n = len(slownik.values())
print(s/n)

# Wartości maksymalne
for n in range(2):
    slownik2 = slownik
    slownik3 = slownik
    if n == 0:
        print("\nOto trzy największe wartości:\n")
    else:
        print("\nOto trzy najmniejsze wartości:\n")
    for i in range(3):
        slownik2 = slownik3

        maxval = max(slownik2.values())
        minval = min(slownik2.values())

        maksimum = [k for k, v in slownik2.items() if v == maxval]
        minimum = [k for k, v in slownik2.items() if v == minval]

        if n == 0:
            # print(f"Wartość nr.{n}")
            print(f"Wartość nr.{i+1}", maksimum[0], slownik2[maksimum[0]])
            slownik2.pop(maksimum[0])
        else:
            # print(f"Wartość nr.{i+1}")
            print(f"Wartość nr.{i+1}", minimum[0], slownik2[minimum[0]])
            slownik2.pop(minimum[0])
        slownik3 = slownik2

duration = time.process_time() - start
print("{0:02f}s".format(duration))
