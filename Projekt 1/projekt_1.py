import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import math

start = time.process_time()
def projectile():
    print("Program 'projectile' do wizuaizowania trajektorii rzutu ukośnego z oporem powietrza postaci F=Bv^2.\n"
          "Aby zobacyzć wizualizację proszę wpisać wymagane dane w podanych jednostkach i w podanym zakresie.\n"
          "Zadany w treści wzór na opór powietrza działa fizycznie tylko dla 'większych' prędkości, więc nie są rekomendowane "
          "prędkości początkowe niższe niż 8-10 m\s\n")
    Vp = float(input("Proszę podać prędkość początkową, najlepiej >10 by być wiernym fizyce [m\s]\n"))
    m = float(input("Proszę podać masę obiektu, najlepiej >= 1, by wiernie oddawać fizykę [kg]\n"))
    h = float(input("Proszę podać początkową wysokość obiektu [m]\n"))
    B = float(input("Proszę podać stałą oporu powietrza B. Dla referencji:\nStała dla pocisku=0.0000146356875,\n"
                    "Stała dla piłeczki baseballowej=0.0007196875,\n"
                    "Stała dla przeciętnego człowieka=0.52828125\n"))
    a_deg = float(input("Proszę podać kąt pod jakim jest wykonywany rzut [deg]\n"))

    # # Przykładowe dane początkowe:
    # Vp = 150  # [m/s]
    # m = 1  # [kg]
    # h = 100  # [m]
    # if h == 0:
    #     h = 0.000000000001
    # B = 0.00315  # [dzikie jednostki]
    # a_deg = 45  # [deg]


    # Stałe
    a = float(np.pi * a_deg / 180)
    g = 9.81  # [m/s^2]
    Vt = np.sqrt(m * g / B)
    Vxp = Vp * np.cos(a)
    Vyp = Vp * np.sin(a)
    b = 10

    # Wzory na zmienne


    def x(t):
        return float(math.pow(Vt, 2) / g * np.log((math.pow(Vt, 2) + g * Vxp * t) / (math.pow(Vt, 2))))


    def vy(t):
        kat = t * g / Vt
        if kat % (np.pi/2) == 0:
            kat = kat + 0.1
        return float(Vt * (Vyp - Vt * np.tan(kat)) / (Vt + Vyp * np.tan(kat)))


    def y(t):
        if t >= Tmax and float(Vt * (Vyp - Vt * np.tan(t * g / Vt)) / (Vt + Vyp * np.tan(t * g / Vt))) >= Vt:
            return float(h + math.pow(Vt, 2) / (2 * g) * np.log((math.pow(Vyp, 2) + math.pow(Vt, 2)) / (2*math.pow(Vt, 2))))
        else:
            return float(h + math.pow(Vt, 2) / (2 * g) * np.log((math.pow(Vyp, 2) + math.pow(Vt, 2)) / (math.pow(float(Vt * (Vyp - Vt * np.tan(t * g / Vt)) / (Vt + Vyp * np.tan(t * g / Vt))), 2) + math.pow(Vt, 2))))


    def y_2(t):
        return float(pow(Vt, 2) / g * np.log(np.cosh(g * (t - Vt) / Vt)))
    def y_par(t):
        return float(h + Vyp*t - 0.5 * g * t**2)
    def x_par(t):
        return float(Vxp * t)

    # Parametry apogeum
    Tmax = (Vt / g) * np.arctan((Vyp / Vt))
    Xmax = x(Tmax)
    Ymax = y(Tmax)
    Apogeum = (Xmax, Ymax, Tmax)

    # Wpisanie w arraye
    if m > 0:
        czas = np.linspace(0, int(x(Tmax)), num=int(x(Tmax)*100))
    else:
        czas = np.linspace(0, int(x(Tmax))*(b/m), num=int(x(Tmax)*100*(1/m)))
    list_x = []
    list_par_x = []
    list_y = []
    list_par_y = []
    t_end = 0
    for t in czas:
        if t <= Tmax:
            dy = y(t)
            dx = x(t)
            list_x.append(dx)
            list_y.append(dy)
        else:
            dy = y(t)
            dx = x(t)
            list_x.append(dx)
            list_y.append(dy)
        dy_par = y_par(t)
        dx_par = x_par(t)
        list_par_y.append(dy_par)
        list_par_x.append(dx_par)
        if dy <= 0.0 and t > 0:
            print("Czas")
            break
        t_end = t

    # # Opcjonalne printu argumentów
    # print(f"m = {m} kg")
    # print(f"alpha[deg] = {a_deg}")
    # print(f"alpha[rad] = {a}")
    # print(f"V początkowa = {Vp} m/s")
    # print(f"V końcowa = {Vt} m/s")
    # print(f"Vy0 = {Vyp} m/s")
    # print(f"Vx0 = {Vxp} m/s")
    # print(f"h_0 = {h} m")
    # print(f"v(0) = {vy(0)}")
    # print(f"Dane dla apogeum: X_ap = {Apogeum[0]} m,Y_ap = {Apogeum[1]} m, Vy(T_ap) = {int(vy(Apogeum[2]))} m/s, T_ap = {Apogeum[2]} s")
    # print(f"Czas lotu to: {t_end} sekund")
    # print(f"Len(x): {len(list_x)}")
    # print(f"Len(czas): {len(czas)}")

    fig, ax = plt.subplots()
    axis = plt.axes(xlim=(0, 2 * x(t_end)), ylim=(0, 2 * Ymax))
    line, = axis.plot([], [], lw=2, color='y')
    dots, = axis.plot([], [], '.', color='b', lw=10)
    axis.set_title("Projectile")
    axis.set_xlabel("Zasięg [m]")
    axis.set_ylabel('Wysokość [m]')
    xdata, ydata = [], []

    def init():
        line.set_data([], [])
        dots.set_data([], [])
        return line,
    def animate(i):
        t = 0.1 * i / (b)
        if y(t) <= 0:
            anim.event_source.stop()
        xval = x(t)
        yval = y(t)

        xdata.append(xval)
        ydata.append(yval)
        line.set_data(xdata, ydata)
        dots.set_data(xdata[i], ydata[i])
        return line, dots,
    ax.set_aspect('equal')
    plt.grid()
    anim = animation.FuncAnimation(fig, animate, init_func = init,
                                   frames = int(len(list_x)*2*b), interval = 1, blit = True)
    plt.show()

projectile()

duration = time.process_time() - start
print("Running time: {0:02f}s".format(duration))
