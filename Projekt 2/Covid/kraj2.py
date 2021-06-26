# import scipy
# import matplotlib as plt
import pandas as pd
import requests

print("Importing the data file, please wait...")
url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
r = requests.get(url, allow_redirects=True)
open('covid.csv', 'wb').write(r.content)
df = pd.read_csv('covid.csv', sep=',')
dic = df.to_dict()
print("Data succesfully imported!")
zakres_pocz = 0
zakres_kon = 30
zakres_calosc = len(list(dic.values())[0])


def cut_col(col):
    kolumna = []
    for i in range(zakres_pocz, zakres_kon):
        # Ta pętla odpowiada za wybór wiersza
        row = []
        for l in list(dic.keys()):
            # Ta pętla odpowiada za dodawanie kolejnych kolumn z ustalonego wiersza
            g = str(dic[f'{l}'][i])
            if g == 'nan':
                g = ''
            row.append(g)
        kolumna.append(row[col])
    return kolumna


def all_unique_elements_of_col_out(beg, end, col):
    res = []
    global zakres_pocz
    global zakres_kon
    tmp1 = zakres_pocz
    tmp2 = zakres_kon
    zakres_pocz = beg
    zakres_kon = end
    lista = cut_col(col)
    for l in range(len(lista)):
        g = str(lista[l])
        if g in res:
            continue
        elif g == 'nan':
            continue
        else:
            res.append(g)
    # print(res)
    zakres_pocz = tmp1
    zakres_kon = tmp2
    return res


def count_el_in_col(beg, end, col):
    res = []
    num = []
    global zakres_pocz
    global zakres_kon
    tmp1 = zakres_pocz
    tmp2 = zakres_kon
    zakres_pocz = beg
    zakres_kon = end
    lista = cut_col(col)
    counter = 0
    for numerator in range(0, len(lista)):
        occurence = str(lista[numerator])
        if occurence in res:
            counter += 1
        elif occurence == 'nan':
            continue
        else:
            res.append(occurence)
            if counter >= 1:
                num.append(counter)
            counter = 1
    num.append(counter)
    # print(res)
    zakres_pocz = tmp1
    zakres_kon = tmp2
    return res, num

print("\nPreprocessing data, please wait...")
rows_per_country = {}
kraje_all = all_unique_elements_of_col_out(zakres_pocz, zakres_calosc, 2)
time_range = all_unique_elements_of_col_out(0, zakres_calosc, 3)
kraje_list, kraje_list_num = count_el_in_col(0, zakres_calosc, 2)
for l in range(len(kraje_list)):
    rows_per_country[f"{kraje_list[l]}"] = kraje_list_num[l]
print("Data ready for use!")

class Kraj:
    global time_range
    global dic
    country = ""
    global kraje_all
    dostepne_kraje = kraje_all

    kraj_pocz = 0
    kraj_konc = 1
    global rows_per_country
    countries_count = rows_per_country

    zakres_pocz = 0
    zakres_kon = 30
    global zakres_calosc

    def __new__(cls, *args, **kwargs):
        return object.__new__(cls)

    def __init__(self, *args):
        kolumny = []
        daty = []
        cases_total = []
        cases_new = []
        total_deaths = []
        new_deaths = []
        total_cases_per_million = []
        new_cases_per_million = []
        total_deaths_per_million = []
        new_deaths_per_million = []
        icu_patients = []
        icu_patients_per_million = []
        hosp_patients = []
        hosp_patients_per_million = []
        new_tests_per_thousand = []
        total_tests_per_thousand = []
        total_vaccinations = []
        people_vaccinated = []
        people_fully_vaccinated = []
        population = []
        # self.time_range = self.all_unique_elements_of_col(0, self.zakres_calosc, 3)
        if len(args) != 0:
            self.country = str(args[0])
            print("Wybrano kraj: " + self.country)
            pocz, konc = self.find_country_range()
            for el in range(0, len(dic)):
                kolumny.append(self.all_el_col_range(pocz, konc, el))
            daty = kolumny[3]
            cases_total = kolumny[4]
            cases_new = kolumny[6]
            total_deaths = kolumny[8]
            new_deaths = kolumny[9]
            total_cases_per_million = kolumny[11]
            new_cases_per_million = kolumny[12]
            total_deaths_per_million = kolumny[14]
            new_deaths_per_million = kolumny[15]
            icu_patients = kolumny[18]
            icu_patients_per_million = kolumny[19]
            hosp_patients = kolumny[20]
            hosp_patients_per_million = kolumny[21]
            new_tests_per_thousand = kolumny[29]
            total_tests_per_thousand = kolumny[28]
            total_vaccinations = kolumny[35]
            people_vaccinated = kolumny[36]
            people_fully_vaccinated = kolumny[37]
            population = kolumny[44]
            print("Obecna ilość chorych w kraju " + self.country + " to: " + str(cases_total[-1]))
            print(pocz)
            print(konc)
            # print(time_range)
            # print(time_range)

        # print(self.dostepne_kraje)

        if self.country not in self.dostepne_kraje:
            choice = input("Nie ma takiego kraju na liście. " +
                           "Czy wyświtlić listę dostępnych krajów? (y/n)")
            if choice == "y":
                print(self.dostepne_kraje)

    def __len__(self):
        return zakres_calosc

    def __getitem__(self, col):
        return self.kolumny[col]

    def __repr__(self):
        return self.cases_total

    def __add__(self, other):
        return self.cases_total + other.cases_total

    def row_range_list(self):
        zakres_wierszy = []
        for i in range(self.zakres_pocz, self.zakres_kon):
            # Ta pętla odpowiada za wybór wiersza
            row = []
            for l in list(dic.keys()):
                # Ta pętla odpowiada za dodawanie kolejnych kolumn z ustalonego wiersza
                g = str(dic[f'{l}'][i])
                if g == 'nan':
                    g = ''
                row.append(g)
            zakres_wierszy.append(row)
        return zakres_wierszy

    def row_range_col(self, col):
        kolumna = []
        for i in range(self.zakres_pocz, self.zakres_kon):
            # Ta pętla odpowiada za wybór wiersza
            row = []
            for l in list(dic.keys()):
                # Ta pętla odpowiada za dodawanie kolejnych kolumn z ustalonego wiersza
                g = str(dic[f'{l}'][i])
                if g == 'nan':
                    g = ''
                row.append(g)
            kolumna.append(row[col])
        return kolumna

    def all_el_col_range(self, beg, end, col):
        kolumna = []
        for i in range(beg, end):
            # Ta pętla odpowiada za wybór wiersza
            row = []
            for l in list(dic.keys()):
                # Ta pętla odpowiada za dodawanie kolejnych kolumn z ustalonego wiersza
                g = str(dic[f'{l}'][i])
                if g == 'nan':
                    g = '0'
                row.append(g)
            kolumna.append(row[col])
        return kolumna

    def all_unique_elements_of_col(self, beg, end, col):
        res = []
        tmp1 = self.zakres_pocz
        tmp2 = self.zakres_kon
        self.zakres_pocz = beg
        self.zakres_kon = end
        lista = self.row_range_col(col)
        for l in range(len(lista)):
            g = str(lista[l])
            if g in res:
                continue
            elif g == 'nan':
                continue
            else:
                res.append(g)
        # print(res)
        self.zakres_pocz = tmp1
        self.zakres_kon = tmp2
        return res

    def count_el_in_col(self, beg, end, col):
        res = []
        num = []
        tmp1 = self.zakres_pocz
        tmp2 = self.zakres_kon
        self.zakres_pocz = beg
        self.zakres_kon = end
        lista = self.row_range_col(col)
        print(lista)
        counter = 0
        for numerator in range(0, len(lista)):
            occurence = str(lista[numerator])
            if occurence in res:
                counter += 1
            elif occurence == 'nan':
                continue
            else:
                res.append(occurence)
                if counter >= 1:
                    num.append(counter)
                counter = 1
        num.append(counter)
        # print(res)
        self.zakres_pocz = tmp1
        self.zakres_kon = tmp2
        return res, num

    def print_row_range(self):
        # for i in range(len(list(dic.values())[0])):
        for i in range(0, self.zakres_kon - self.zakres_pocz):
            print(','.join(self.row_range_list()[i]))
        if self.zakres_pocz <= self.zakres_kon:
            del i

    # def find_date(self, data):
    def find_country_range(self):
        kraj = self.country
        global kraje_list
        global kraje_list_num
        beg = 0
        end = 0
        for order in range(len(kraje_list)):
            if kraje_list[order] != kraj:
                continue
            else:
                sum = 0
                for mul in range(0, order):
                    sum += kraje_list_num[mul]
                beg = sum
                end = beg + kraje_list_num[order]
        return beg, end
