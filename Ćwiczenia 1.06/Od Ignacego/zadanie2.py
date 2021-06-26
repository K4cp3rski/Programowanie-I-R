import numpy as np
def pierwiastek(dx, dy, x, f, n = 1000):
    x1 = x
    x = x
    while n > 0:
        h = f(x)
        if np.abs(h) < dy:
            return x
        g = (f(x+h)-h)/h
        x1 = x
        x = x - h/g
        n-=1
    print('przekroczono liczbe przyblizen')
def f(x):
    return np.sin(x)
print(pierwiastek(0.1,0.01,2.1,f))


