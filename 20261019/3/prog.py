from collections import Counter


width = int(input())
counts = Counter()

while line := input():
    cleaned = ''.join(char if char.isalpha() else ' ' for char in line)
    for word in cleaned.lower().split():
        if len(word) == width:
            counts[word] += 1

if counts:
    largest = max(counts.values())
    print(*sorted(word for word, count in counts.items() if count == largest))
