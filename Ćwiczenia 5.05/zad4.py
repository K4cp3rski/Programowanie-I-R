import re

tekst = input("Proszę wpisać tekst do sprawdzenia:\n")

# tekst = "Pżecież ja już mam dosyć tej analizy"

tekst_split = re.split('\s', tekst)
tekst_out = ""

for k in tekst_split:
    if len(re.findall(r'\w*[PpBbTtDdKkGgJjWw Ch ch]ż\w*', k)) != 0:
        consent = input(f"Znaleziono błąd w słowie {k}, czy poprawić go? (y/n)\n")
        if consent == 'y':
            print("Poprawiono błąd")
            k = re.sub('ż', 'rz', k)
        else:
            print("Nie poprawiono błędu")
    tekst_out += k + " "

print(f'Tekst wejściowy: "{tekst}"')
print(f'Tekst wyjściowy: "{tekst_out}"')
