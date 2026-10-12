from decimal import Decimal


def esum(N, one):
    s = one
    fact = 1

    for n in range(1, N + 1):
        fact *= n
        s += one / fact

    return s


print(esum(20, 1.0))
print(esum(20, Decimal(1)))