t = int(input())

for i in range(t):
    n = int(input())
    p = list(reversed(range(1, n + 1)))
    p[n - 1], p[(n // 2)] = p[(n // 2)], p[n - 1]

    print(" ".join(list(map(str, p))))
