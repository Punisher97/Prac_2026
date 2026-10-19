expression = input()
a, b = eval(input()), eval(input())

first = eval(expression, {"x": a, "y": b})
second = eval(expression, {"x": b, "y": a})

print(f"{first} {second}")
