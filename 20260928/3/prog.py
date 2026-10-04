first = list(eval(input()))
n = len(first)

matr1 = [first]

for i in range(n - 1):
    matr1.append(list(eval(input())))

matr2 = []

for i in range(n):
    matr2.append(list(eval(input())))

res = []

for i in range(n):
    row = []
    for j in range(n):
        x = 0
        for k in range(n):
            x += matr1[i][k] * matr2[k][j]
        row.append(x)
    res.append(row)

for i in range(n):
    for j in range(n):
        if j != n - 1:
            print(res[i][j], end=",")
        else:
            print(res[i][j])