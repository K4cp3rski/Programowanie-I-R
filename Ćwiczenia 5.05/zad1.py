import re

tekst = "Jest dzień 6.05, godzina 9.08, jadę pociągiem na szczepienie. A teraz jest godzina 15.31 i wracam do domu zaszczepiony i szczęśliwy."
# tekst = input("Proszę wpisać tekst do analizy\n")

output = {}
analiza = {}

# Szukanie Samogłosek
output['samogloski'] = re.findall(r"[AaĄąEeĘęIiOoÓóUuYy]", tekst)

# Spółgłoski
bez_sam = re.findall(r"[^AaĄąEeĘęIiOoÓóUuYy]", tekst)
spolgloski_pom = re.findall(r"[A-Za-z]", ''.join(bez_sam))

output['spolgloski'] = spolgloski_pom

# Cyfry
output['cyfry'] = re.findall(r"[0-9]", tekst)

# Szukanie spacji
output['spacje'] = re.findall(r"\s", tekst)

for k in output.keys():
    analiza[f'{k}'] = len(output[f"{k}"])

print(analiza)


