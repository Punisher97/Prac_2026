class Maze:
    def __init__(self, n):
        size = 2 * n + 1
        self.grid = [["█"] * size for _ in range(size)]
        for y in range(1, size, 2):
            for x in range(1, size, 2):
                self.grid[y][x] = "·"

    def __str__(self):
        return "\n".join("".join(row) for row in self.grid)

    def __setitem__(self, key, value):
        x, part, y1 = key
        y, x1 = part.start, part.stop
        if y == y1:
            for i in range(min(x, x1), max(x, x1)):
                self.grid[2*y+1][2*i+2] = value
        elif x == x1:
            for i in range(min(y, y1), max(y, y1)):
                self.grid[2*i+2][2*x+1] = value

    def __getitem__(self, key):
        x, part, y1 = key
        start = 2*x+1, 2*part.start+1
        end = 2*part.stop+1, 2*y1+1
        stack = [start]
        seen = {start}
        while stack:
            x, y = stack.pop()
            if (x, y) == end:
                return True
            for nx, ny in ((x-1, y), (x+1, y), (x, y-1), (x, y+1)):
                if self.grid[ny][nx] == "·" and (nx, ny) not in seen:
                    seen.add((nx, ny))
                    stack.append((nx, ny))
        return False


if __name__ == "__main__":
    import sys
    exec(sys.stdin.read())
