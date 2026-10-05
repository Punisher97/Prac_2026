def average(a, *args):
    return sum(args) / (len(args) + 1)
print(average(1, 2, 3, 4, 15.5))