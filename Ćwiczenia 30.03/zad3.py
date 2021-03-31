import time

start = time.process_time()
ciag = str(input("Proszę wpisać ciąg znaków do zakodowania:\n"))


def kodowanie(cosiek):
    dl = len(cosiek)
    kod = ""
    klucz = []
    for i in range(0, dl):
        tmp = ord(cosiek[i])
        klucz.append(len(str(tmp)))
        kod += f"{tmp}"
    return klucz, kod


def dekodowanie(*args):
    wzor = str(args[0])
    klucze = list(args[1])
    odk = ""
    tmp = 0
    for i in klucze:
        tmp_str = ""
        for g in range(tmp, tmp+i):
            tmp_str += wzor[g]
        odk += f"{chr(int(tmp_str))}"
        tmp += i
    return str(odk)


kod_main = kodowanie(ciag)[0]
zakodowane = kodowanie(ciag)[1]
print(kod_main, "\n", kodowanie(ciag)[1], "\n")
dek = str(input("Czy chcesz odkodować ten ciąg? (y/n):\n"))

if dek == "y":
    # szyfr = str(input("Jaki ciąg ma być odkodowany?\n"))
    print(dekodowanie(zakodowane, kod_main))

duration = time.process_time() - start
print("{0:02f}s".format(duration))
