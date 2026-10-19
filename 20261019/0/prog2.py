import string
from timeit import Timer

def count_letters(s):
    glas = {"e", "y", "u", "i", "o", "a"}
    letters = string.ascii_lowercase
    consonants = set(letters) - glas

    return len(s & glas), len(s & consonants)

text = input()
stext = set(text.lower())
number, elapsed = Timer(lambda: count_letters(stext)).autorange()
print(f"{number} loops, {elapsed / number} sec per loop")
print(*count_letters(stext))