# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
#
# x = np.linspace(0, 10, 100)
# y = np.sin(x)
#
# fig, ax = plt.subplots()
# line, = ax.plot(x, y, color='k')
# a = 5
# ax.grid()
# def update(num, x, y, line):
#     line.set_data(x[:num], y[:num])
#     line.axes.axis([0, 2*a, -1, 1])
#     return line,
#
# ani = animation.FuncAnimation(fig, update, len(x), fargs=[x, y, line],
#                               interval=25, blit=False)
# ani.save('test.gif')
# plt.show()

import numpy as np
import matplotlib.pyplot as plt

def projectile(V_initial, theta, bouyancy=True, drag=True):
    g = 9.81
    m = 1
    C = 0.47
    r = 0.5
    S = np.pi*pow(r, 2)
    ro_mars = 0.0175

    time = np.linspace(0, 100, 10000)
    tof = 0.0
    dt = time[1] - time[0]
    bouy = ro_mars*g*(4/3*np.pi*pow(r, 3))
    gravity = -g * m
    V_ix = V_initial * np.cos(theta)
    V_iy = V_initial * np.sin(theta)
    v_x = V_ix
    v_y = V_iy
    r_x = 0.0
    r_y = 0.0
    r_xs = list()
    r_ys = list()
    r_xs.append(r_x)
    r_ys.append(r_y)
    # This gets a bit 'hand-wavy' but as dt -> 0 it approaches the analytical solution.
    # Just make sure you use sufficiently small dt (dt is change in time between steps)
    for t in time:
        F_x = 0.0
        F_y = 0.0
        if (bouyancy == True):
            F_y = F_y + bouy
        if (drag == True):
            F_y = F_y - 0.5*C*S*ro_mars*pow(v_y, 2)
            F_x = F_x - 0.5*C*S*ro_mars*pow(v_x, 2) * np.sign(v_y)
        F_y = F_y + gravity

        r_x = r_x + v_x * dt + (F_x / (2 * m)) * dt**2
        r_y = r_y + v_y * dt + (F_y / (2 * m)) * dt**2
        v_x = v_x + (F_x / m) * dt
        v_y = v_y + (F_y / m) * dt
        if (r_y >= 0.0):
            r_xs.append(r_x)
            r_ys.append(r_y)
        else:
            tof = t
            r_xs.append(r_x)
            r_ys.append(r_y)
            break

    return r_xs, r_ys, tof

v = 30
theta = np.pi/4

fig = plt.figure(figsize=(8,4), dpi=300)
r_xs, r_ys, tof = projectile(v, theta, True, True)
plt.plot(r_xs, r_ys, 'g:', label="Gravity, Buoyancy, and Drag")
r_xs, r_ys, tof = projectile(v, theta, False, True)
plt.plot(r_xs, r_ys, 'b:', label="Gravity and Drag")
r_xs, r_ys, tof = projectile(v, theta, False, False)
plt.plot(r_xs, r_ys, 'k:', label="Gravity")
plt.title("Trajectory", fontsize=14)
plt.xlabel("Displacement in x-direction (m)")
plt.ylabel("Displacement in y-direction (m)")
plt.ylim(bottom=0.0)
plt.legend()
plt.show()

# import numpy as np
# from scipy.integrate import odeint
# import scipy.constants as SPC
# import matplotlib.pyplot as plt
#
# V_initial = 30 # m/s
# theta = np.pi/6 # 30
# g = 3.711
# m = 1 # I assume this is your mass
# C = 0.47
# r = 0.5
# ro_mars = 0.0175
#
# t_flight = 2*(V_initial*np.sin(theta)/g)
# t = np.linspace(0, t_flight, 200)
#
# pos0 = [0, 0]
# v0 = [np.cos(theta) * V_initial, np.sin(theta)  * V_initial]
#
# def f(vector, t, C, r, ro_mars, apply_bouyancy=True, apply_resistance=True):
#     x, y, x_prime, y_prime = vector
#
#     # volume and surface
#     V = np.pi * 4/3 * r**3
#     S = np.pi*pow(r, 2)
#
#     # net weight bouyancy
#     if apply_bouyancy:
#         Fb = (ro_mars * V - m) * g *np.array([0,1])
#     else:
#         Fb = -m  * g * np.array([0,1])
#
#     # velocity vector
#     v = np.array([x_prime, y_prime])
#
#     # drag force - corrected to be updated based on current velocity
# #    Ft = -0.5*C*S*ro_mars*pow(V_initial, 2)
#     if apply_resistance:
#         Ft = -0.5*C*S*ro_mars* v *np.linalg.norm(v)
#     else:
#         Ft = np.array([0, 0])
#
#     # resulting acceleration
#     x_prime2, y_prime2 = (Fb + Ft) / m
#
#     return x_prime, y_prime, x_prime2, y_prime2
#
# sol = odeint(f, pos0 + v0 , t, args=(C, r, ro_mars))
# plt.plot(sol[:,0], sol[:, 1], 'g', label='tray')
# plt.legend(loc='best')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid()
# plt.show()