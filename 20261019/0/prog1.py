from timeit import Timer


def main():
    snippet = input()
    number, elapsed = Timer(snippet).autorange()
    print(f"{number} loops, {elapsed / number} sec per loop")



main()
