from math import floor

t = int(input())

for i in range(t):
    inpt = input().split()
    n = int(inpt[0])
    k = int(inpt[1])

    step1 = n * k
    if step1 % (n - 1) > 0:
        print(int(floor(step1 / (n - 1))))
    else:
        print(int(step1 / (n - 1) - 1))
