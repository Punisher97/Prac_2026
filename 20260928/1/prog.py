l = []
M, N = eval(input())
for i in range(M, N):
    for j in range (2, i // 2 + 1):
        if i % j == 0:
            break
    else:
        l.append(i)
print(l)
        

            