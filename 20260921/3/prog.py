n = int(input())

i = n
while i <= n + 2:
    j = n
    while j <= n + 2:
        res = i * j
        sum = 0
        tmp = res
        while tmp > 0:
            sum += tmp % 10
            tmp //= 10
        if sum == 6:
            res = ":=)"
        print(i, "*", j , "=", res, end=' ')
        j += 1
    i += 1
    print()