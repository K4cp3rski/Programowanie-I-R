deltas = [[1,0,-1],[0,1,-1],[-1,1,0],[-1,0,1],[0,-1,1],[1,-1,0]]
class HexGrid():
    def __init__(self, radius):
        self.radius = radius
        self.tiles = {(0, 0, 0): "X"}
        for r in range(radius):
            a = 0
            b = -r
            c = +r
            for j in range(6):
                num_of_hexas_in_edge = r
                for i in range(num_of_hexas_in_edge):
                    a = a+deltas[j][0]
                    b = b+deltas[j][1]
                    c = c+deltas[j][2]
                    self.tiles[a,b,c] = "X"

    def show(self):
        l = []
        for y in range(20):
            l.append([])
            for x in range(60):
                l[y].append(".")
        for (a,b,c), tile in self.tiles.iteritems():
            l[self.radius-1-b][a-c+(2*(self.radius-1))] = self.tiles[a,b,c]
        mapString = ""
        for y in range(len(l)):
            for x in range(len(l[y])):
                mapString += l[y][x]
            mapString += "\n"
        print(mapString)