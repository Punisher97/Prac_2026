def gen_adders(n):
    adders = []
    for i in range(n):
        def adder(x):
            return x + i
        adders.append(adder)
    return(adders)