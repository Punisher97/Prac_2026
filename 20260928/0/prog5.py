matr = []
while s := input():
	a = list(eval(s))
	matr.append(a)

if all(len(s) == len(matr) for s in matr):
	for i in range(len(matr)):
		for j in range(i + 1, len(matr)):
			matr[i][j], matr[j][i] = matr[j][i], matr[i][j]
	for el in matr:
		print(el)
else:
	print("Not square")
