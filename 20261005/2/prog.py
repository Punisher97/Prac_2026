def sub(a, b):

    if type(a) in [int, float, complex]:
        return a-b

    elif isinstance(a, tuple):
        ans = []
        for el in a:
            if el not in b:
                ans.append(el)
        return(tuple(ans))

    elif isinstance(a, list):
        ans = []
        for el in a:
            if el not in b:
                ans.append(el)
        return(ans)


print(sub(*eval(input())))