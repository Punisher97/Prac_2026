from fractions import Fraction


def make_fraction(token):
    if '/' in token:
        return Fraction(token)
    return Fraction(int(token), 1)


def evaluate_polynomial(coeffs, x):
    total = 0
    for coef in coeffs:
        total = total * x + make_fraction(coef)
    return total


def main():
    values = input().replace(',', ' ').split()
    x0 = make_fraction(values[0])
    wanted = make_fraction(values[1])
    degree_a = int(values[2])

    a_coeffs = values[3:3 + degree_a + 1]
    pos = 3 + degree_a + 1
    degree_b = int(values[pos])
    b_coeffs = values[pos + 1:pos + 1 + degree_b + 1]

    numerator = evaluate_polynomial(a_coeffs, x0)
    denominator = evaluate_polynomial(b_coeffs, x0)

    if denominator == 0:
        print(False)
    else:
        print(numerator / denominator == wanted)


main()
