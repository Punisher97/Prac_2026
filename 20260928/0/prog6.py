a, b = eval(input())
for i in range(a, b + 1):
	if '3' not in str(i) and i % 2:
		print(i)
