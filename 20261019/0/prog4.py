from collections import Counter
from timeit import Timer

def count_words(s):
    words = s.split()
    word_count = Counter(words)
    return word_count

text = input()
print(count_words(text))
number, elapsed = Timer(lambda: count_words(text)).autorange()
print(f"{number} loops, {elapsed / number} sec per loop")
