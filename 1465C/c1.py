# Time Limit on Test Case 4

import sys

input = sys.stdin.readline

t = int(input())


def check_free_square(coordinate, positions):
    free = True
    for loc in positions:
        if loc == coordinate:
            continue
        else:
            if (
                loc[0] == coordinate[0]
                or loc[0] == coordinate[0]
                or loc[1] == coordinate[0]
                or loc[1] == coordinate[1]
            ):
                free = False
    return free


for i in range(t):
    n, m = list(map(int, input().split()))
    pos = []
    for i in range(m):
        pos.append(tuple(map(int, input().split())))

    if m == 1:
        print(1)
        continue
    else:
        for loc in pos:
            if loc[0] == loc[1]:
                m -= 1
                continue
        for loc in pos:
            if loc[1] == loc[0]:
                continue

            if check_free_square(loc, pos) == True:
                m -= 1
                break

        print(m + 1)
