while i := input():
	if int(i) == 13:
		print("THIRTEEN!")
		break
	if int(i) % 2 == 0:
		print(i)
else:
	print("n0 13!")
