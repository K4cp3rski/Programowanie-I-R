import time
import matplotlib.pyplot as plt

start = time.process_time()
h = 12  # Wysokość dużego prostokąta
w = 12  # Szerokość dużego prostokata
b = 1  # Początkowy punkt rysunku
d = 0.8  # Odległosć między prostokątami

fig, ax = plt.subplots()
x = [b, b, b+w, b+w, b]
y = [h, h/2, h/2, h, h]
x1 = [b, b, b + (w - 2*d)/3, b + (w - 2*d)/3, b]
y1 = [h/2 - d, 0, 0, h/2 - d, h/2 - d]
x2 = [b + (w - 2*d)/3 + d, b + (w - 2*d)/3 + d, b + (w - 2*d)*2/3 + d, b + (w - 2*d)*2/3 + d, b + (w - 2*d)/3 + d]
x3 = [b + (w - 2*d)*2/3 + 2*d, b + (w - 2*d)*2/3 + 2*d, b + w, b + w, b + (w - 2*d)*2/3 + 2*d]
plt.plot(x, y, 'k-', linewidth=1)
plt.plot(x1, y1, 'k-', linewidth=1)
plt.plot(x2, y1, 'k-', linewidth=1)
plt.plot(x3, y1, 'k-', linewidth=1)
plt.axis('off')

plt.show()


duration = time.process_time() - start
print("{0:02f}s".format(duration))