from math import ceil

t = int(input())

for i in range(t):
    n, x = list(map(int, input().split()))

    if n <= 2:
        print(1)
    else:
        print(ceil((n - 2) / x) + 1)
