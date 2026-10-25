text = input()
pairs = set()

for left, right in zip(text, text[1:]):
    if left.isalpha() and right.isalpha():
        pairs.add((left.lower(), right.lower()))

print(len(pairs))
