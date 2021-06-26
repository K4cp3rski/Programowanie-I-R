from concurrent.futures import ThreadPoolExecutor
import time
import urllib.request


def download(n_pliku):
    f = f'{n_pliku}.jpg'
    url = f'https://www.fuw.edu.pl/~gonz/dydaktyka/pr/c10/pictures/{f}'
    urllib.request.urlretrieve(url, f'{f}')
    print(f'Plik o numerze {n_pliku} sciagniety!')

def pobierz():
    for i in range(10):
        download(i)


t = [i for i in range(10)]
print(t)

start = time.time()
pobierz()
end = time.time()

print("Duration: %.3f s" % (end-start))

start = time.time()
res = list(map(download, t))
end = time.time()

print("Duration: %.3f s" % (end-start))

start = time.time()
with ThreadPoolExecutor(10) as pool:
    wynik = list(pool.map(download, t))
end = time.time()

print("Duration: %.3f s" % (end-start))