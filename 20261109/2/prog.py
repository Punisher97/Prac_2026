class Triangle:
    def __init__(self, a, b, c):
        self.points = tuple(a), tuple(b), tuple(c)

    @staticmethod
    def turn(a, b, p):
        return ((b[0] - a[0]) * (p[1] - a[1])
                - (b[1] - a[1]) * (p[0] - a[0]))

    def __abs__(self):
        area = abs(self.turn(*self.points))
        return area / 2 if area else 0

    def __bool__(self):
        return abs(self) > 0

    def __lt__(self, other):
        return abs(self) < abs(other)

    def edges(self):
        a, b, c = self.points
        return (a, b), (b, c), (c, a)

    def __contains__(self, other):
        if not other:
            return True
        if not self:
            return False
        for p in other.points:
            signs = [self.turn(a, b, p) for a, b in self.edges()]
            if min(signs) < 0 < max(signs):
                return False
        return True

    def __and__(self, other):
        if not self or not other:
            return False
        for first, second in ((self, other), (other, self)):
            side = self.turn(*first.points)
            for a, b in first.edges():
                if all(side * self.turn(a, b, p) < 0 for p in second.points):
                    return False
        return True


if __name__ == "__main__":
    import sys
    exec(sys.stdin.read())
