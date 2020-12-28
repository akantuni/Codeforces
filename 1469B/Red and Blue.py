t = int(input())

for i in range(t):
    n = int(input())
    red = list(map(int, input().split()))
    m = int(input())
    blue = list(map(int, input().split()))

    def get_ps(arr):
        ps = [arr[0]]

        for i, item in enumerate(arr):
            if i == 0:
                continue
            else:
                ps.append(ps[i - 1] + item)
        return ps

    rx = max(get_ps(red))
    bx = max(get_ps(blue))

    print(max(rx, bx, 0, rx + bx))
