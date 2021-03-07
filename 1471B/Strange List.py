t = int(input())

for k in range(t):
    n, x = list(map(int, input().split()))
    a = list(map(int, input().split()))

    b = [(1, item) for item in a]

    ans = 0

    for count, item in b:
        if item % x == 0:
            b.append((x * count, item // x))
        else:
            break

    for count, item in b:
        ans += count * item

    print(ans)
