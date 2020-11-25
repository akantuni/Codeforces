import string
from math import ceil
import sys

input = sys.stdin.readline

alphabet = string.ascii_lowercase

t = int(input())

for i in range(t):
    n, a, b = list(map(int, input().split()))
    fragment = alphabet[:b]

    final = (fragment * ceil(n / b))[:n]

    print(final)
