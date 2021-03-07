t = int(input())

for case in range(t):
    n = int(input())
    n = list(map(str, range(2, n + 1)))
    print(len(n))
    print(" ".join(n))
