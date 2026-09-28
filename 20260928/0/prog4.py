l = eval(input())
for i in l:
	if i % 2 == 1:
		print(i)
		break
else:
	print(l[0])
