t = int(input())

for i in range(t):
    n, k = list(map(int, input().split()))

    if k > n:
        print("NO")
    elif n == k:
        print("YES\n" + "1 " * (n - 1) + "1")
    elif n % 2 == 1 and k % 2 == 0:
        print("NO")
    elif k == 1:
        print("YES\n" + str(n))
    else:
        if (n - ((k - 1) * 2)) <= 0:
            if (n - ((k - 1) * 1)) <= 0:
                print("NO")
            else:
                if (n - ((k - 1) * 1)) % 2 == 1:
                    print("YES\n" + ("1 " * (k - 1)) + (str(n - ((k - 1) * 1))))
                else:
                    print("NO")
        else:
            if (n - ((k - 1) * 2)) % 2 == 0:
                print("YES\n" + ("2 " * (k - 1)) + (str(n - ((k - 1) * 2))))
            else:
                print("YES\n" + ("1 " * (k - 1)) + (str(n - ((k - 1) * 1))))
