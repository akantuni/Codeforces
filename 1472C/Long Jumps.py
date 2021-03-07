t = int(input())

for k in range(t):
    n = int(input()) - 1
    a = list(map(int, input().split()))
    obj = {}

    for i in range(len(a) - 1, -1, -1):
        ind = i
        total = 0
        x = obj.get(ind)
        while ind <= n:
            if x is None:
                total += a[ind]
            else:
                total += x
                break
            ind += a[ind]
        obj.update({i: total})

    print(max(obj.values()))
