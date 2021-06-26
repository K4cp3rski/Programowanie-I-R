import numpy as np
from triangle_grid import triangle_grid_count, triangle_grid_points


def triangle_grid_display(t, ng, tg, filename):
    # *****************************************************************************80
    #
    ## TRIANGLE_GRID_DISPLAY displays grid points inside a triangle.
    #
    #  Licensing:
    #
    #    This code is distributed under the GNU LGPL license.
    #
    #  Modified:
    #
    #   09 April 2015
    #
    #  Author:
    #
    #    John Burkardt
    #
    #  Parameters:
    #
    #    Input, real T(3,2), the coordinates of the vertices of the triangle.
    #
    #    Input, integer NG, the number of grid points inside the triangle.
    #
    #    Input, real TG(NG,2), the grid points.
    #
    #    Input, string FILENAME, the name of the plotfile to be created.
    #
    import matplotlib.pyplot as plt
    import numpy as np
    #
    #  Plot the outline of the triangle.
    #
    tx = np.zeros(4)
    ty = np.zeros(4)

    tx[0] = t[0, 0];
    tx[1] = t[1, 0];
    tx[2] = t[2, 0];
    tx[3] = t[0, 0];
    ty[0] = t[0, 1];
    ty[1] = t[1, 1];
    ty[2] = t[2, 1];
    ty[3] = t[0, 1];

    plt.plot(tx, ty, linewidth=2.0, color='r')
    #
    #  Plot the gridpoints.
    #
    plt.plot(tg[0:ng, 0], tg[0:ng, 1], 'bs', marker='.')
    #
    #  Cleanup and annotate.
    #
    plt.xlabel('<---X--->')
    plt.ylabel('<---Y--->')
    plt.title('Grid points in triangle')
    plt.grid(True)
    plt.axis('equal')
    plt.gca().set_aspect("equal")

    plt.savefig(filename)

    plt.show()
    plt.clf()

    print('')
    print('  Graphics data saved in file "%s"' % (filename))

    return


n = 20

R = 10

a = 2 * R * np.sqrt(3)

t = np.array([ \
    [-a/2, -R],\
    [a/2, -R], \
    [0.0, 2*R]])

# print(t)

filename = 'triangle_grid_points.png'

ng = triangle_grid_count(n)

tg = triangle_grid_points(n, t)

triangle_grid_display(t, ng, tg, filename)

import hexgrid
hg = hexgrid.HexGrid(R)
# print(hg.tiles)


# Linki do ogarnięcia przy stawianiu heksagonalnego układu współrzędnych:
# https://www.redblobgames.com/grids/hexagons/
# https://github.com/RedFT/Hexy
# https://stackoverflow.com/questions/2049196/generating-triangular-hexagonal-coordinates-xyz
# https://stackoverflow.com/questions/11373122/best-way-to-store-a-triangular-hexagonal-grid-in-python
# https://people.sc.fsu.edu/~jburkardt/py_src/disk_grid/disk_grid.html
# https://people.sc.fsu.edu/~jburkardt/py_src/triangle_grid/triangle_grid.html