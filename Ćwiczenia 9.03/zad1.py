import time

start = time.process_time()

lista = input("Podaj wyraz do sprawdzenia: \n")
print(f"Twój wyraz to {lista}")


def palindrom(lista):
    dl = len(lista)
    # print(f"Długość to {dl}")
    wyraz = list(lista)
    # print(f"Lista to {wyraz}")
    p = 0
    pal = False
    while p is not (dl-p-1):
        if wyraz[p] == wyraz[-(p+1)]:
            pal = True
            p = p+1
            continue
        else:
            pal = False
            break
    if pal:
        print("Jest to palindrom")
    else:
        print("Nie jest to palindrom")

duration = time.process_time() - start

palindrom(lista)
print("{0:02f}s".format(duration))