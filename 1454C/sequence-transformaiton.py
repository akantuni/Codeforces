import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n = int(input())
    seq = list(map(int, input().split()))

    prev = None

    final = []

    for elem in seq:
        if elem != prev:
            final.append(elem)
            prev = elem

    frequencies = {}
    if len(final) == 1:
        print(0)
        continue

    for j in range(len(final)):
        elem = final[j]
        frequencies[elem] = frequencies.get(elem, 0) + 1

    frequencies[final[0]] -= 1
    frequencies[final[-1]] -= 1

    print(min(frequencies.values()) + 1)
