import time

start = time.process_time()
d = input("Podaj nazwę pliku do otwarcia:\n")
typ = input("Czy jest to plik binarny? (y/n)\n")
typ_nowy = 0
if typ == "y":
    typ = "rb"
    typ_nowy = "wb"
else:
    typ = "r"
    typ_nowy = "w"
plik = open(d, typ)
nowy = open("kopia_"+d, typ_nowy)

while True:
    b = plik.read(1)
    if not b:
        break
    nowy.write(b)

plik.close()
nowy.close()

print("Zakończono kopiowanie")

duration = time.process_time() - start
print("{0:02f}s".format(duration))