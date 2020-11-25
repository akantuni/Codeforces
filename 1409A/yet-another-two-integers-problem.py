t = int(input())

for i in range(t):
    a, b = sorted(list(map(int, input().split())))
    moves = (b - a) // 10
    if (b - a) % 10 > 0:
        moves += 1
    print(moves)
