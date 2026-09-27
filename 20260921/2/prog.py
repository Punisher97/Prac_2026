sum = 0
while sum <= 21:
    a = int(input())
    if  a > 0:
        sum += a
    else:
        print(a)
        break
if sum > 21:
    print(sum)