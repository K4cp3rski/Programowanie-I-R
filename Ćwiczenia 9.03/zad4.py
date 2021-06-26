import time


start = time.process_time()

a = int(input("Jaką liczbę chcesz potęgować? \n"))
n = int(input("Do jakiej potęgi chcesz ją podnieść? \n"))
# print(f"a={a},n={n}")


def Pot(a,n):
    if n == 0:
      return 1
    elif n % 2 == 1 :
      return a * (Pot(a, (n - 1) / 2)) ** 2
    else:
        return a * (Pot(a, n / 2)) ** 2

print(f"{a}^{n} = {Pot(a,n)}")

duration = time.process_time() - start
print("{0:02f}s".format(duration))