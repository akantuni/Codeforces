from math import ceil
from operator import lt, gt

t = int(input())

for k in range(t):
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))

    a_max = a


    mx = 0
    mn = 0

    for item in a_max:
        mx += ceil(item / x)
    mn += ceil(sum(a) / x)

    print(mn, mx)



