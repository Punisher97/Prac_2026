l = list(eval(input()))

for i in range(len(l) - 1):
    swapped = False
    for j in range (len(l) - i - 1):
        if l[j] ** 2 % 100 > l[j + 1] ** 2 % 100:
            l[j], l[j + 1] = l[j + 1], l[j]
            swapped = True
    if not swapped:
        break
print(l)