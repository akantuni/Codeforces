t = int(input())
for i in range(t):
    a, b, x, y, n = list(map(int, input().split()))
    diff_a = a - x
    diff_b = min((b - y), n)
    temp_a = a
    temp_b = b
    temp_n = n

    mn = 0

    if diff_a >= temp_n and 0 < (temp_a - temp_n) * temp_b:
        mn = (temp_a - temp_n) * temp_b
    else:
        temp_a -= diff_a
        temp_n -= diff_a
        if diff_b >= temp_n:
            temp_b -= temp_n
        else:
            temp_b -= diff_b
        if 0 < temp_a * temp_b:
            mn = temp_a * temp_b

    diff_b = b - y
    diff_a = a - x

    if diff_b >= n:
        if 0 < (b - n) * a < mn:
            mn = (b - n) * a
    else:
        b -= diff_b
        n -= diff_b
        if diff_a >= n:
            diff_a = n
        a -= diff_a
        if 0 < a * b < mn:
            mn = a * b

    print(mn)
