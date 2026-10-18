from math import *


def scale(a, b, A, B, x):
    return (x - a) / (b - a) * (B - A) + A


def main():
    pieces = input().replace(',', ' ').split()
    width = int(pieces[0])
    height = int(pieces[1])
    a = float(pieces[2])
    b = float(pieces[3])
    formula = pieces[4]

    screen = [[' ' for _ in range(width)] for _ in range(height)]

    sample_count = 1000
    y_values = [eval(formula) for x in [scale(0, sample_count - 1, a, b, i) for i in range(sample_count)]]
    y_max = max(y_values)
    y_min = min(y_values)

    previous = None
    for col in range(width):
        x = scale(0, width - 1, a, b, col)
        y = eval(formula)
        row = int(scale(y_min, y_max, height - 1, 0, y))

        if previous is None:
            screen[row][col] = '*'
        else:
            for r in range(min(row, previous), max(row, previous) + 1):
                screen[r][col] = '*'
        previous = row

    print('\n'.join(''.join(line) for line in screen))


main()
