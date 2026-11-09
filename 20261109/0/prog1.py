


class Rectangle:
    rectcnt = 0

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.__class__.rectcnt += 1
        setattr(self, f"rect_{self.rectcnt}", self.rectcnt)

    def __str__(self):
        return (f"({self.x1}, {self.y1}), ({self.x2}, {self.y2}), "
                f"rectcnt={self.rectcnt}")

    def area(self):
            return abs((self.x2 - self.x1) * (self.y2 - self.y1))
        

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __mul__(self, number):
        return self.__class__(
            self.x1 * number,
            self.y1 * number,
            self.x2 * number,
            self.y2 * number,
        )

    def __rmul__(self, number):
        return self.__mul__(number)

    def __getitem__(self, idx):
        coord = (
            (self.x1, self.y1),
            (self.x1, self.y2),
            (self.x2, self.y2),
            (self.x2, self.y1),
        )
        return coord[idx]

    def __bool__(self):
        return self.area() > 0

    def __del__(self):
        self.__class__.rectcnt -= 1
        print(f"Remaining rectangles: {self.rectcnt}")

    def __iter__(self):
        pass