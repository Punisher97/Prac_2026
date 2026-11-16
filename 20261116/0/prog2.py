# if __name__ == "__main__":
#     while True:
#         try:
#             number = int(input("Введите целое число: "))
#         except ValueError:
#             print("Это не целое число. Попробуйте ещё раз.")
#         else:
#             break

try:
    try:
        raise KeyError("Hello")
    except Exception as e:
        raise RuntimeError("World")
except Exception as e2:
    print(e2, e2.__context__, e2.__cause__)

def div(a, b, eps):
    if abs(b) < eps:
        raise ValueError("b is too small")
    return a / b