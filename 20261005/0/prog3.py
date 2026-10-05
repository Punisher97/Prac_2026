def req(N):
    while N != 0:
        N -= 1
        req(N)
req(int(input()))