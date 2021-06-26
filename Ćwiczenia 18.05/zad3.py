from concurrent.futures import ThreadPoolExecutor
import time
from functools import lru_cache

# N = 30

# Ten dekorator jest potężny, z nim można brać zakres nawet i do N=100000 dla pierwszych dwóch.
# Dla ThreadPool N=1000 coś się psuje w ostatniej funkcji, przez to, że ona robi w losowej kolejności
N = 100000
# N = 1000


@lru_cache
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)


def licz_fib():
    res = []
    for i in range(N):
        res.append(fib(i))
        print(fib(i))


t = [i for i in range(N)]

start = time.time()
licz_fib()
end = time.time()

print("Duration: {:e} s".format(end-start))

# start = time.time()
# res = list(map(fib, t))
# # for i in res:
#     # print(i)
# end = time.time()
#
# print("Duration: {:e} s".format(end-start))

# start = time.time()
# with ThreadPoolExecutor(10) as pool:
#     wynik = list(pool.map(fib, t))
#     # for i in wynik:
#     #     print(i)
# end = time.time()

# print("Duration: {:e} s".format(end-start))
