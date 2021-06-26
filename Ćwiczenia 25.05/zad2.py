from functools import reduce

fib = lambda n: reduce(lambda x, _: x + [x[-2] + x[-1]], range(n - 2), [0, 1])

fibsum = lambda n: reduce(lambda x, y: x+y, fib(n))

fib_parzyste = lambda n: list(filter(lambda x: x % 2 == 0, fib(n)))

fib_nieparzyste = lambda n: list(filter(lambda x: x % 2 != 0, fib(n)))

n = 15
print(fib(n))
print(fibsum(n))
print(fib_parzyste(n))
print(fib_nieparzyste(n))
