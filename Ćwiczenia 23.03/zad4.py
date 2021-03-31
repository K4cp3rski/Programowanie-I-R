import time

start = time.process_time()

lista = [1, 2, 3]

def numDiff(lista):
    dl = len(lista)
    rozne = []
    for i in range(dl):
        if lista[i] not in rozne:
            rozne.append(lista[i])
        else:
            continue
    return len(rozne)
print("Liczba różnych elementów w liście to:", numDiff(lista))

duration = time.process_time() - start
print("{0:02f}s".format(duration))