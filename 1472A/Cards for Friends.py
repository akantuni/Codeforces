t = int(input())

for i in range(t):
    w, h, n = list(map(int, input().split()))

    timesw = 1
    timesh = 1
    if w % 2 == 0:
        w2 = w
        while w2 % 2 == 0:
            timesw *= 2
            w2 /= 2
    if h % 2 == 0:
        h2 = h
        while h2 % 2 == 0:
            timesh *= 2
            h2 /= 2
    total = timesh * timesw
    if total >= n:
        print("YES")
    else:
        print("NO")
