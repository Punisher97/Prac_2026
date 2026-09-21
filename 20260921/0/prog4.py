i = 1
ans = 0
a = int(input())
while a != 0:
	ans += (a == i)
	i += 1
	a = int(input())
print(ans)
