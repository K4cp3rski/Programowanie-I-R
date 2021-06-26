import re

maile = "mój adres email to cyb1neq@gmail.com, oraz k.cybinski@student.uw.edu.pl"

maile_out = []

mail_split = re.split(' ', maile)

for k in mail_split:
    new = re.findall('[^\s?,:*/]+@.+[\.]+[a-zA-Z][a-zA-Z]+', k)
    if len(new) != 0:
        maile_out.append(new[0])

for k in maile_out:
    print("Znaleziono mail:", k)
