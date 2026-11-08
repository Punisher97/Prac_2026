from itertools import islice, tee


def slide(seq, n):
    if n <= 0:
        return

    copies = tee(seq, n)
    for i in range(n):
        for _ in range(i):
            next(copies[i], None)

    index = 0
    while True:
        window = list(islice(copies[index % n], n))
        if not window:
            return
        yield from window
        index += 1
