from math import ceil
import sys
input = sys.stdin.readline

t = int(input())
for k in range(t):
    n = int(input())
    final = "989" + ("0123456789" * ceil(n / 10))
    print(final[:n])
