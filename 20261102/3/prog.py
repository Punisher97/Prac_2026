from itertools import product


def sacred(n):
    result = []
    for word in product('ORT', repeat=n):
        s = ''.join(word)
        if s.count('TOR') == 2:
            result.append(s)
    return sorted(result)
