import time

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
print(f"{lista}")

for l in range(0, dl):
    if lista[l] > 1:
        for g in range(2, lista[l]):
            if (lista[l] % g) == 0:
                if lista[l] == 2:
                    prime = lista[l]
                prime = 0
                break
            else:
                prime = lista[l]
    if prime > 0:
        prime_list.append(prime)

print(prime_list)


duration = time.process_time() - start
print("{0:02f}s".format(duration))
