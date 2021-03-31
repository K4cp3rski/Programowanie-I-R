import time

start = time.process_time()

roman = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC", 50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 1: "I"}
n = int(input("Proszę wpisać całkowitą liczbę dodatnią do konwersji:\n"))
konwertowana = n

k = sorted(roman.keys(), reverse=True)
# print(k)
rzymska = ""
for i in k:
    while i <= n:
        rzymska += roman[i]
        n -= i
print(f"Liczba {konwertowana} zapisana liczbami rzymskimi to {rzymska}")


duration = time.process_time() - start
print("{0:02f}s".format(duration))