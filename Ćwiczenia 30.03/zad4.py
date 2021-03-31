import time

start = time.process_time()
# ciag = str(input("Proszę wpisać ciąg znaków do zakodowania:\n"))

def kodowanie(cosiek):
    dl = len(cosiek)
    kod = ""
    klucz = []
    b = 5
    for i in range(0, dl):
        tmp = ord(cosiek[i]) + b
        if tmp not in range(65, 90) or range(97, 122):
            if tmp in range(97 + b, 123 + b):
                if tmp == 32 + b:
                    continue
                if tmp > 122:
                    tmp = (tmp - 123) + 97
            elif tmp in range(65 + b, 91 + b):
                if tmp == 32 + b:
                    continue
                if tmp >= 90:
                    tmp = (tmp - 91) + 65
        klucz.append(len(str(tmp)))
        kod += f"{tmp}"
    return klucz, kod

def ascii(cosiek):
    dl = len(cosiek)
    kod = ""
    klucz = []
    for i in range(0, dl):
        tmp = ord(cosiek[i])
        if tmp == 32:
            tmp = 37
        klucz.append(len(str(tmp)))
        kod += f"{tmp}"
    return klucz, kod

def dekodowanie(*args):
    wzor = str(args[0])
    klucze = list(args[1])
    b = 5
    odk = ""
    tmp = 0
    for i in klucze:
        tmp_str = ""
        for g in range(tmp, tmp+i):
            tmp_str += wzor[g]
        ghg = int(int(tmp_str) - b)
        if ghg not in range(65 + b, 90) or range(97 + b, 122):
            if ghg in range(96-b, 97):
                if ghg <= 97 + b:
                    ghg = 122 - (96 - ghg)
            else:
                if ghg == 32:
                    ghg = 32
                elif ghg in range(64 - b, 65):
                    if ghg <= 65 + b:
                        ghg = 90 - (64 - ghg)
        odk += f"{chr(ghg)}"
        tmp += i
    return str(odk)

def odczyt(*args):
    wzor = str(args[0])
    klucze = list(args[1])
    odk = ""
    tmp = 0
    for i in klucze:
        tmp_str = ""
        for g in range(tmp, tmp+i):
            tmp_str += wzor[g]
        if tmp_str == "37":
            tmp_str = "32"
        odk += f"{chr(int(tmp_str))}"
        tmp += i
    return str(odk)

def szyfrowanie_pliku(nazwa_pliku):
    plik = open(f"{nazwa_pliku}", "r")
    output = open("zakodowane.txt", "w")
    keys = open("klucze.txt", "w")
    linie = plik.read().splitlines()
    for i in linie:
        out = odczyt(kodowanie(i)[1], kodowanie(i)[0])
        key = ''.join(map(str, kodowanie(i)[0]))
        output.write(out+"\n")
        keys.write(key+"\n")
    output.close()
    plik.close()
    keys.close()


def deszyfracja_pliku(nazwa_pliku_odszyfrowanie, nazwa_klucze):
    plik = open(f"{nazwa_pliku_odszyfrowanie}", "r")
    output = open("odkodowane.txt", "w")
    keys = open(f"{nazwa_klucze}", "r")
    linie = plik.read().splitlines()
    klucze = keys.read().splitlines()
    for i in range(len(linie)):
        wejscie = str(linie[i])
        kluczyk = list(klucze[i])
        kluczyk = [int (i) for i in kluczyk]
        out = dekodowanie(ascii(wejscie)[1], kluczyk)
        output.write(out+"\n")
    output.close()
    plik.close()
    keys.close()

pytanie = input("Chcesz szyfrować plik, czy go deszyfrować? (1/2)\n")

if pytanie == "1":
    nazwa_pliku = str(input("Jak się nazywa plik?\n"))
    szyfrowanie_pliku(nazwa_pliku)
    print("Plik został zapisany jako 'zakodowane.txt', a jego klucze w pliku 'klucze.txt'\n")
elif pytanie == "2":
    nazwa_pliku_odszyfrowanie = str(input("Jak się nazywa plik do odszyfrowania?\n"))
    nazwa_klucze = str(input("Jak się nazywa plik z kluczami?\n"))
    deszyfracja_pliku(nazwa_pliku_odszyfrowanie, nazwa_klucze)
    print("Odszyfrowany plik został zapisany jako 'odszyfrowane.txt'")
else:
    print("Niepoprawna wartość")

    # kod_main = kodowanie(ciag)[0]
    # zakodowane = kodowanie(ciag)[1]
    # print(kod_main, "\n", kodowanie(ciag)[1])
    # # print("\n")
    # print(f"Zakodowany napis to: {odczyt(zakodowane,kod_main)}")

    # if str(input("Czy chcesz, by odkodować ten napis? (y/n)\n")) == "y":
    #     print(f"Odkodowany napis to: {dekodowanie(zakodowane, kod_main)}")

duration = time.process_time() - start
print("{0:02f}s".format(duration))
