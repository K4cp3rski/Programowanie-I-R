from concurrent.futures import ThreadPoolExecutor
import time
from functools import lru_cache


@lru_cache
def nwd(t0):
    x = t0[0]
    y = t0[1]
    if y == 0:
        return x
    r = int(x % y)
    t1 = (y, r)
    return nwd(t1)


t = [(1963309, 2265973), (2030677, 3814172), (1551645, 2229620), (2039045, 2020802)]

start = time.time()
res = list(map(nwd, t))
end = time.time()

print("Duration: {:e} s".format(end-start))

start = time.time()
pool = ThreadPoolExecutor(max_workers=4)
wynik = list(pool.map(nwd, t))
end = time.time()

print("Duration: {:e} s".format(end-start))

print(res)
print(wynik)
