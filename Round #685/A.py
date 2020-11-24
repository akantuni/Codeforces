import math
t = int(input())

for i in range(t):
    n = int(input())
    if n <= 3:
        print(n - 1)
    else:
        print(2 + (n & 1))



