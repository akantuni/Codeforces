t = int(input())

for i in range(t):
    n, x, y = list(map(int, input().split()))
    diff = 0
    x_pos = 0
    for j in range(1, n):
        if (y - x) % (n - j) == 0:
            diff = int((y - x) / (n - j))
            x_pos = j - 1
            break

    mn = int(x - diff * x_pos)
    while mn <= 0:
        mn += diff

    memo = []

    for _ in range(n):
        memo.append(mn)
        mn += diff

    print(" ".join(list(map(str, sorted(memo)))))
