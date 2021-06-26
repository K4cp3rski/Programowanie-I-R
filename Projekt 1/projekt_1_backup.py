import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

start = time.process_time()

# Dane początkowe:
Vp = 100  # [m/s]
m = 1  # [kg]
h = 500  # [m]
B = 0.00315  # [dzikie jednostki]
a_deg = 45  # [deg]
b = 100

# Stałe
a = float(np.pi * a_deg / 180)
g = 9.81  # [m/s^2]
Vt = np.sqrt(m * g / B)
Vxp = Vp * np.cos(a)
Vyp = Vp * np.sin(a)
# Vyp = 15

# Wzory na zmienne


def x(t):
    return float(math.pow(Vt, 2) / g * np.log((math.pow(Vt, 2) + g * Vxp * t) / (math.pow(Vt, 2))))


def vy(t):
    return float(Vt * (Vyp - Vt * np.tan(t * g / Vt)) / (Vt + Vyp * np.tan(t * g / Vt)))


def y(t):
    return float(h + math.pow(Vt, 2) / (2 * g) * np.log((math.pow(Vyp, 2) + math.pow(Vt, 2)) / (math.pow(float(Vt * (Vyp - Vt * np.tan(t * g / Vt)) / (Vt + Vyp * np.tan(t * g / Vt))), 2) + math.pow(Vt, 2))))


def y_2(t):
    # return float(Ymax - Vt * (t - Tmax))
    return float(pow(Vt, 2) / g * np.log(np.cosh(g * (t - Vt) / Vt)))
    # return float(Ymax - (math.pow(Vt, 2) / (2 * g) * np.log((math.pow(Vyp, 2) + math.pow(Vt, 2)) / (2 * math.pow(Vt, 2)))))
    # return (Ymax - 1/2 * g * (t-Tmax)**2)
def y_par(t):
    return float(h + Vyp*t - 0.5 * g * t**2)
def x_par(t):
    return float(Vxp * t)

# Parametry apogeum
Tmax = (Vt / g) * np.arctan((Vyp / Vt))
Xmax = x(Tmax)
Ymax = y(Tmax)
# Ymax = (math.pow(Vt, 2)/(2 * g)) * np.log((math.pow(Vt, 2) + math.pow(Vyp, 2)) / math.pow(Vt, 2))
Apogeum = (Xmax, Ymax, Tmax)

# Wpisanie w arraye
czas = np.linspace(0, int(x(Tmax)), num=int(x(Tmax)*10))
list_x = []
list_par_x = []
list_y = []
list_par_y = []
t_end = 0
for t in czas:
    dy = y(t)
    dx = x(t)
    list_x.append(dx)
    list_y.append(dy)
    # dy_par = y_par(t)
    # dx_par = x_par(t)
    # list_par_y.append(dy_par)
    # list_par_x.append(dx_par)
    if dy <= 0.0:
        print("Czas")
        # t_end = t
        break
    t_end = t

print(f"m = {m} kg")
print(f"alpha[deg] = {a_deg}")
print(f"alpha[rad] = {a}")
print(f"V początkowa = {Vp} m/s")
print(f"V końcowa = {Vt} m/s")
print(f"Vy0 = {Vyp} m/s")
print(f"Vx0 = {Vxp} m/s")
print(f"h_0 = {h} m")
print(f"v(0) = {vy(0)}")
print(f"Dane dla apogeum: X_ap = {Apogeum[0]} m,Y_ap = {Apogeum[1]} m, Vy(T_ap) = {int(vy(Apogeum[2]))} m/s, T_ap = {Apogeum[2]} s")
print(f"Czas lotu to: {t_end} sekund")
print(f"Len(x): {len(list_x)}")
print(f"Len(czas): {len(czas)}")

fig, ax = plt.subplots()
axis = plt.axes(xlim=(0, 2 * x(t_end)),
                ylim=(0, 2 * Ymax))
line, = axis.plot([], [], lw=2, color='y')
dots, = axis.plot([], [], '.', color='b', lw=10)
axis.set_xlabel("Zasięg [m]")
axis.set_ylabel('Wysokość [m]')
xdata, ydata = [], []

def init():
    line.set_data([], [])
    dots.set_data([], [])
    return line,
# ax.set(xlim=(0, 2 * x(t_end)), ylim=(0, 2 * Ymax))
def animate(i):
    # t is a parameter which varies
    # with the frame number
    t = 0.1 * i / (0.5*b)
    if y(t) <= 0:
        anim.event_source.stop()
    # x, y values to be plotted
    xval = x(t)
    yval = y(t)
    # xval = list_x[i]
    # yval = list_y[i]
    # appending values to the previously
    # empty x and y data holders
    xdata.append(xval)
    ydata.append(yval)
    line.set_data(xdata, ydata)
    dots.set_data(xdata[i], ydata[i])
    # line.set_data(list_x[:t], list_y[:t])
    return line, dots,
plt.grid()
anim = animation.FuncAnimation(fig, animate, init_func = init,
                               frames = int(len(list_x)*2*b), interval = 1, blit = True)

#
#
# def update(num, x, y, line):
#     line.set_data(x[num], y[num])
#     # line.axes.axis([0, 10, 0, 1])
#     return line
# ani = animation.FuncAnimation(fig, update, len(list_x), fargs=[x, y, line], interval=25, blit=False)
# # ani.save("test2.gif")


plt.show()

duration = time.process_time() - start
print("Running time: {0:02f}s".format(duration))
