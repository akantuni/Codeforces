t = int(input())

for i in range(t):
    n, m = list(map(int, input().split()))

    grid = []
    for i in range(n):
        row = list(map(int, input().split()))
        for num in row:
            grid.append(num)

    mn = float("inf")
    amount = 0
    total = 0

    for number in grid:
        if number < 0:
            amount += 1
        if abs(number) < mn:
            mn = abs(number)
        total += abs(number)

    if amount % 2 == 0:
        print(total)
    else:
        print(total - 2 * mn)
