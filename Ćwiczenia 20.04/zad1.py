wejscie = input("Proszę podać sekwencję do sprawdzenia:\n")

lista = wejscie.split(',')
wyniki = []

for i in lista:
    if int(i, 2) % 5 == 0:
        # print(int(i, 2))
        wyniki.append(i)
    else:
        # print(int(i, 2))
        continue

print(wyniki)
