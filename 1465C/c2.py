# Time Limit on Test Case 4

import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, m = list(map(int, input().split()))
    pos = []
    for i in range(m):
        pos.append(tuple(map(int, input().split())))

    if m == 1:
        print(1)
        continue
    else:
        x = []
        y = []
        final = []
        for loc in pos:
            x_value = loc[0]
            y_value = loc[1]
            if x_value == y_value:
                m -= 1

            x.append(x_value)
            y.append(y_value)

        for num in x:
            if num not in y:
                final.append(num)

        if len(final) > 0:
            print(m)
        else:
            print(m + 1)
