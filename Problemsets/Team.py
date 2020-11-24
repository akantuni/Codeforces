n = int(input())

total = 0

for i in range(n):
    agree = sum(list(map(int, input().split())))
    if agree > 1:
        total += 1


print(total)
