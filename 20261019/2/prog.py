from math import *


def main():
    functions = {}
    line_count = 0

    while True:
        line = input()
        line_count += 1

        if line.startswith(':'):
            name, *parameters, expression = line[1:].split()
            functions[name] = parameters, expression
            continue

        name, *rest = line.split(maxsplit=1)
        if name == 'quit':
            template = eval(rest[0])
            print(template.format(len(functions) + 1, line_count))
            break

        parameters, expression = functions[name]
        if len(parameters) == 1:
            arguments = [rest[0]]
        elif parameters:
            arguments = rest[0].split()
        else:
            arguments = []

        values = [eval(argument) for argument in arguments]
        variables = dict(zip(parameters, values))
        print(eval(expression, globals(), variables))


main()
