import math
t = int(input())

for i in range(t):
    n = int(input())
    if n == 1:
        print(0)
    elif n == 2:
        print(1)
    elif n == 3:
        print(2)
    elif n % 2 == 1:
        print(3)
    else:
        print(2)


