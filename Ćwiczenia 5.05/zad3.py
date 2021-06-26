import re

tekst = "Nie tak, nie tak, nie tak; To nie tak, nie tak, nie tak"
tekst_out = ""

tekst_list = re.split('\s', tekst)
for k in tekst_list:
    if re.search("tak", k) != None:
        if re.search("tak", k).group() != "nie":
            k = re.sub('tak', 'nie', k)
    elif re.search("Nie", k) != None:
        if re.search("Nie", k).group() != "Tak":
            k = re.sub('Nie', 'Tak', k)
    elif re.search("nie", k) != None:
        if re.search("nie", k).group() != "tak":
            k = re.sub('nie', 'tak', k)
    tekst_out += k + " "


print(tekst)
print(tekst_out)
