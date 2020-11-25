from math import sqrt, floor

t = int(input())

for i in range(t):
    n = int(input())
    if n == 1:
        print(0)
    else:
        if floor(sqrt(n)) ** 2 == n:
            print(floor(sqrt(n) * 2 - 2))
        else:
            print(floor(sqrt(n) * 2 - 1))
