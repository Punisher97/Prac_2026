from timeit import Timer


def count_words_dict(text):
    counts = {}
    for word in text.split():
        counts[word] = counts.setdefault(word, 0) + 1
    return counts


text = input()
print(count_words_dict(text))
number, elapsed = Timer(lambda: count_words_dict(text)).autorange()
print(f"{number} loops, {elapsed / number} sec per loop")
