import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import time

load_start = time.process_time()

print("Importing the data file, please wait...")
url = 'https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv'
r = requests.get(url, allow_redirects=True)
open('covid.csv', 'wb').write(r.content)
df = pd.read_csv('covid.csv', sep=',')
dic = df.to_dict()
print("Data succesfully imported!")

load_dur = time.process_time() - load_start
print("Data loading time: {0:02f}s".format(load_dur))

zakres_pocz = 0
zakres_kon = 30
zakres_calosc = len(list(dic.values())[0])

def make_ticklabels_invisible(fig):
    for i, ax in enumerate(fig.axes):
        ax.text(0.5, 0.5, "ax%d" % (i+1), va="center", ha="center")
        for tl in ax.get_xticklabels() + ax.get_yticklabels():
            tl.set_visible(False)


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

process_start = time.process_time()

print("\nPreprocessing data, please wait...")
rows_per_country = {}
kraje_all = all_unique_elements_of_col_out(zakres_pocz, zakres_calosc, 2)
time_range = all_unique_elements_of_col_out(0, zakres_calosc, 3)
kraje_list, kraje_list_num = count_el_in_col(0, zakres_calosc, 2)
for l in range(len(kraje_list)):
    rows_per_country[f"{kraje_list[l]}"] = kraje_list_num[l]
print("Data ready for use!")

process_dur = time.process_time() - process_start
print("Preprocessing time: {0:02f}s".format(process_dur))

class Kraj:
    global time_range
    global dic
    country = ""
    global kraje_all
    dostepne_kraje = kraje_all
    nazwy_kolumn = list(dic.keys())
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
    new_vaccinations = []
    people_vaccinated = []
    people_fully_vaccinated = []
    population = []

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
        # self.time_range = self.all_unique_elements_of_col(0, self.zakres_calosc, 3)
        if len(args) != 0:
            self.country = str(args[0])
            print("Wybrano kraj: " + self.country)
            pocz, konc = self.find_country_range()
            self.kolumny = []
            for el in range(0, len(dic)):
                self.kolumny.append(self.all_el_col_range(pocz, konc, el))
            self.daty = self.kolumny[3]
            self.cases_total = self.kolumny[4]
            self.cases_new = self.kolumny[5]
            self.total_deaths = self.kolumny[8]
            self.new_deaths = self.kolumny[9]
            self.total_cases_per_million = self.kolumny[11]
            self.new_cases_per_million = self.kolumny[12]
            self.total_deaths_per_million = self.kolumny[14]
            self.new_deaths_per_million = self.kolumny[15]
            self.icu_patients = self.kolumny[18]
            self.icu_patients_per_million = self.kolumny[19]
            self.hosp_patients = self.kolumny[20]
            self.hosp_patients_per_million = self.kolumny[21]
            self.new_tests_per_thousand = self.kolumny[29]
            self.total_tests_per_thousand = self.kolumny[28]
            self.total_vaccinations = self.kolumny[35]
            self.people_vaccinated = self.kolumny[36]
            self.people_fully_vaccinated = self.kolumny[37]
            self.new_vaccinations = self.kolumny[38]
            self.population = self.kolumny[44]
            if len(self.new_deaths) != 0:
                deaths_avg = self.seven_day_avg("new_deaths")
                self.save_columns("new_deaths")
                import os
                import errno

                filename = f"./death_stats/{self.country}_deaths_stats.txt"
                if not os.path.exists(os.path.dirname(filename)):
                    try:
                        os.mkdir(os.path.dirname(filename))
                    except OSError as exc:  # Guard against race condition
                        if exc.errno != errno.EEXIST:
                            raise
                with open(filename, "w") as f:
                    f.write(f"{self.country} deaths 7-day avg: " + str(deaths_avg) + "\n")
                    with open(f"{self.country}_columns_['new_deaths'].csv", 'r') as inp:
                        for line in inp:
                            f.write(line)
                    f.close()
                os.remove(f"{self.country}_columns_['new_deaths'].csv")


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
        if len(self.total_vaccinations) >= 3:
            return (f"{self.country} - " + "Liczba nowych przypadków dziś to " + str(self.cases_new[-1]) + "\n" +
                    "Liczba zaszczepionych to " +
                    str(max(self.total_vaccinations[-1], self.total_vaccinations[-2], self.total_vaccinations[-3]) + "\n"))
        elif len(self.total_vaccinations) >= 2:
            return (f"{self.country} - " + "Liczba nowych przypadków dziś to " + str(self.cases_new[-1]) + "\n" +
                    "Liczba zaszczepionych to " +
                    str(max(self.total_vaccinations[-1], self.total_vaccinations[-2]) + "\n"))
        elif len(self.total_vaccinations) >= 1:
            return (f"{self.country} - " + "Liczba nowych przypadków dziś to " + str(self.cases_new[-1]) + "\n" +
                    "Liczba zaszczepionych to " +
                    str(self.total_vaccinations[-1]) + "\n")
        else:
            return (f"{self.country} - " + "Liczba nowych przypadków dziś to " + str(self.cases_new[-1]) + "\n" +
                    "Liczba zaszczepionych to 0")

    def __add__(self, other):
        dluzsza = []
        krotsza = []
        if len(self.cases_new) > len(other.cases_new):
            dluzsza = self.cases_new
            krotsza = other.cases_new
        else:
            dluzsza = other.cases_new
            krotsza = self.cases_new

        print(f"{-len(krotsza)}")
        for i in range(-len(krotsza), 0, 1):
            dluzsza[i] = str(float(dluzsza[i]) + float(krotsza[i]))

        return list(dluzsza)
        # return f"Suma dziennych przypadków z obszarów {self.country} i {other.country} to: " + self.cases_new[-1] + other.cases_new[-1]

    __radd__ = __add__

    def plot_cases(self, visible=True, merged=True):
        if not merged:
            x = np.array(self.daty)
            y1 = []
            y2 = []
            for l in self.cases_new:
                y1.append(float(l))
            for l in self.cases_total:
                y2.append(float(l))

            y1 = np.array(y1)
            y2 = np.array(y2)

            gs = gridspec.GridSpec(2, 2)
            fig = plt.figure(f"Wykresy dziennej i całkowitej liczby przypadków w obszarze: {self.country}", figsize=(14, 8), frameon=False, facecolor='white', edgecolor='black')
            ax = fig.add_subplot(gs[:, 0])
            ax2 = fig.add_subplot(gs[:, 1])
            # ax.set_xlabel('Daty')
            ax.set_ylabel('Dzienna liczba nowych przypadków')
            ax.plot(x, y1, 'b', label='Dzienna liczba nowych przypadków')

            # ax2.set_xlabel('Daty')
            ax2.set_ylabel('Całkowita liczba przypadków')
            ax2.plot(x, y2, 'y', label='Całkowita liczba przypadków')

            ax.set_xticks(np.append(np.arange(0, len(x), len(x)/35), len(x)))
            ax.set_yticks(np.append(np.arange(0, max(y1), max(y1)/30), float(y1[-1:])))
            ax.tick_params(axis='x', labelrotation=45)

            ax2.set_xticks(np.append(np.arange(0, len(x), len(x)/35), len(x)))
            ax2.set_yticks(np.append(np.arange(0, max(y2), max(y2)/30), float(y2[-1:])))
            ax2.tick_params(axis='x', labelrotation=45)

            plt.suptitle(f"Wykresy dziennej i całkowitej liczby przypadków w obszarze: {self.country}")
            ax3 = fig.add_subplot()
            plt.axis('off')
            ax.grid()
            ax2.grid()

        else:
            x = np.array(self.daty)
            y1 = []
            y2 = []
            for l in self.cases_new:
                y1.append(float(l))
            for l in self.cases_total:
                y2.append(float(l))

            y1 = np.array(y1)
            y2 = np.array(y2)

            fig = plt.figure(f"Wykresy dziennej i całkowitej liczby przypadków w obszarze: {self.country}",
                             figsize=(14, 8), frameon=False, facecolor='white', edgecolor='black')
            ax = fig.add_subplot(1,1,1)
            ax2 = ax.twinx()
            # ax.set_xlabel('Daty')
            ax.set_ylabel('Dzienna liczba nowych przypadków', color='b')
            ax.plot(x, y1, 'b', label='Dzienna liczba nowych przypadków')

            # ax2.set_xlabel('Daty')
            ax2.set_ylabel('Całkowita liczba przypadków', color='cyan')
            ax2.plot(x, y2, 'cyan', label='Całkowita liczba przypadków', )

            ax.set_xticks(np.append(np.arange(0, len(x), len(x) / 35), len(x)))
            ax.set_yticks(np.append(np.arange(0, max(y1), max(y1) / 30), float(y1[-1])))
            ax.tick_params(axis='x', labelrotation=45)

            # ax2.set_xticks(np.append(np.arange(0, len(x), len(x) / 35), len(x)))
            ax2.set_yticks(np.append(np.arange(0, max(y2), max(y2) / 30), float(y2[-1])))
            # ax2.tick_params(axis='x', labelrotation=45)

            plt.suptitle(f"Wykresy dziennej i całkowitej liczby przypadków w obszarze: {self.country}")
            # ax3 = fig.add_subplot()
            # plt.axis('off')
            ax.grid()
            ax2.grid()

        plt.tight_layout()
        import os
        import errno

        filename = f"./plots/"
        if not os.path.exists(os.path.dirname(filename)):
            try:
                os.mkdir(os.path.dirname(filename))
            except OSError as exc:  # Guard against race condition
                if exc.errno != errno.EEXIST:
                    raise

        if visible:
            # print(visible)
            plt.show()
            fig.savefig(f"./plots/plots_{self.country}.pdf")
        else:
            # print(visible)
            plt.close(fig)
            fig.savefig(f"./plots/plots_{self.country}.pdf")



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

    def seven_day_avg(self, nazwa_kolumny):
        args = nazwa_kolumny
        sum = 0
        dl = len(args)
        res = [args]
        for g in range(len(dic.keys())):
            if list(dic.keys())[g] == nazwa_kolumny:
                res.append(list(self.kolumny[g]))
            else:
                continue

        if len(res[1]) == 0:
            return 0
        elif len(res[1]) < 7:
            c = len(res[1])
            for i in range(-c, 0):
                sum += float(res[1][i])
            return float(sum/c)
        for i in range(-7, 0):
            sum += float(res[1][i])
        avg = float(sum/7)
        return float(avg)
        # return res

    def save_columns(self, *args):
        dl = len(args)
        res = [list(args)]
        numerki = []
        for i in range(dl):
            name = args[i]
            for g in range(len(dic.keys())):
                if list(dic.keys())[g] == name:
                    res.append(self.kolumny[g])
                    numerki.append(g)
                else:
                    continue
        if len(res) != 0:
            # res = pd.DataFrame(res[1:], columns=res[0])
            pom = []
            for elementy in range(len(res[1])):
                pom.append([])
                for num in range(dl):
                    pom[elementy].append(res[num+1][elementy])
            res = pd.DataFrame(pom, columns=res[0])
            for n in range(len(numerki)):
                numerki[n] = self.nazwy_kolumn[numerki[n]]
            res.to_csv(f"{self.country}_columns_{numerki}.csv", index=False)
        return numerki, res
