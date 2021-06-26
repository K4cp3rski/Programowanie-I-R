import kraj as cl
import time

Kraje = []
index = 0

print("Loading takes about 2 mins, please wait.")
start = time.process_time()
for name in cl.Kraj.dostepne_kraje:
    index += 1
    Kraje.append(cl.Kraj(f"{name}"))
dur = time.process_time() - start
print("List computing time: {0:02f}s".format(dur))
del name, start, dur

# Obiekt klasy z danymi dla Polski
PL = Kraje[166]
BE = Kraje[20]

# Wywołana metoda do zapisu kolumny o podanym tytule
PL.save_columns("population_density")
PL.save_columns("population_density", "people_fully_vaccinated", "new_cases")

# Wywołanie metody do wyliczania średniej tygodniowej z podanej kolumny
avg = PL.seven_day_avg("new_cases")
print(f"Tygodniowa średnia nowych przypadków w {PL.country} to: {avg}")

# Wywołanie metody do wycinania kolumny
col = PL[3]
print(f"Wszystkie daty w zbiorze danych dla {PL.country} to : {col}")
print(f"Pierwsza wpisana data dla {PL.country} to {col[0]} a najnowsza to {col[-1]}")

# Wywołanie metody do rysowania wykresu zależności dziennych przypadków i całkowitych przypadków od czasu
PL.plot_cases()
BE.plot_cases()

