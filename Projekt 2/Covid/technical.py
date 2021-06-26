import scipy
import matplotlib as plt
import pandas as pd
import requests



url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
r = requests.get(url, allow_redirects=True)
open('covid.csv', 'wb').write(r.content)
df = pd.read_csv('covid.csv', sep=',')
dic = df.to_dict()

# print(len(list(dic.values())[0]))
zakres = 300


def print_row(zakres):
    # for i in range(len(list(dic.values())[0])):
    for i in range(zakres):
        # Ta pętla odpowiada za wybór wiersza
        row = ""
        for l in list(dic.keys()):
            # Ta pętla odpowiada za dodawanie kolejnych kolumn z ustalonego wiersza
            g = str(dic[f'{l}'][i])
            if g == 'nan':
                g = ''
            row += g + ','
        print(row)
    del g, i, l


res = []

for l in range(len(dic['location'])):
    g = str(dic['location'][l])
    if g in res:
        continue
    elif g == 'nan':
        continue
    else:
        res.append(g)

# print(res)


