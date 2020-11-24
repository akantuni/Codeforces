n = int(input())

for i in range(n):
    n, m = list(map(int, input().split()))
    tiles = []
    symmetric = False
    for j in range(n):
        a, b = list(map(int, input().split()))
        c, d = list(map(int, input().split()))
        if b == c:
            symmetric = True
        tiles.append([[a, b], [c, d]])

    if symmetric == False:
        print("NO")
    elif m % 2 != 0:
        print("NO")
    else:
        print("YES")
