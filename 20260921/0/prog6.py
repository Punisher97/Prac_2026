while a := input():
	match int(a):
		case "1":
			print("one")
		case "2":
			print("two")
		case "3":
			print("three")
		case var if var % 2 == 0:
			print("chetn")
		case odd:
			print(odd, "- nechet")
