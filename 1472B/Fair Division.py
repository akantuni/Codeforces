t = int(input())

for i in range(t):
    n = int(input())
    ls = input().split()

    one = ls.count("1")
    two = ls.count("2")

    if one % 2 == 0 and one > 0:
        print("YES")
    elif one == 0 and two % 2 == 0:
        print("YES")
    else:
        print("NO")
