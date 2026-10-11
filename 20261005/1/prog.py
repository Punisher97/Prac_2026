def Pareto(*args):
    ans = []

    for a, b in args:
        for c, d in args:
            if c >= a and d >= b and (c > a or d > b): # a, b доминируется c, d
                break
        else:
            ans.append((a, b))
    return tuple(ans)

tuples = eval(input())
print(Pareto(*tuples))