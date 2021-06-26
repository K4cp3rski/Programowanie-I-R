class Polynomial:
    def __init__(self, *args):
        rank=len(args)
        while rank and args[rank-1]==0:
            rank-=1
        self.coeffs = args[:rank] if args[:rank] else (0,)
    def __repr__(self):
        return "Polynomial(*"+str(self.coeffs)+")"
    def __str__(self):
        result = ""
        for o, c in enumerate(self.coeffs):
            if result and c>0:
                result += "+"
            if c:
                result += str(c)
                if o>0:
                    result += "*z"
                if o>1:
                    result += "^"+str(o)
        return result if result else "0"
    def __add__(self, other):
        if isinstance(other, Polynomial):
            result = [0]*max(len(self.coeffs), len(other.coeffs))
            for o, c in enumerate(self.coeffs):
                result[o] += c
            for o, c in enumerate(other.coeffs):
                result[o] += c
        else:
            result = list(self.coeffs)
            result[0] += other
        return Polynomial(*result)
    __radd__ = __add__
    def __sub__(self, other):
        result = [0]*max(len(self.coeffs), len(other.coeffs))
        for o, c in enumerate(self.coeffs):
            result[o] += c
        for o, c in enumerate(other.coeffs):
            result[o] -= c
        return Polynomial(*result)
    def __mul__(self, other):
        if isinstance(other, Polynomial):
            result = [0]*(len(self.coeffs) + len(other.coeffs) - 1)
            for o1, c1 in enumerate(self.coeffs):
                for o2, c2 in enumerate(other.coeffs):
                    result[o1+o2] += c2*c1
        else:
            result = [other*c for c in self.coeffs]
        return Polynomial(*result)
    __rmul__ = __mul__
    def __eq__(self, other):
        return self.coeffs == other.coeffs
    def __call__(self, other):
        result = 0
        for i in reversed(self.coeffs):
            result = other*result + i
        return result
