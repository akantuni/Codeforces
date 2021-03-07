t = int(input())

for i in range(t):
    n0, n1, n2 = list(map(int, input().split()))

    final = ""

    if n2 > 0:
        final += "1" * (n2 + 1)

    if n0 > 0:
        final += "0" * (n0 + 1)

    if n0 > 0 and n2 > 0:
        n1 -= 1
    elif n0 == 0 and n2 == 0:
        n1 += 1

    if len(final) == 0 or final[-1] == "0":
        final += ("10" * n1)[:n1] if n1 > 0 else ("10" * n1)
    else:
        final += ("01" * n1)[:n1]
    print(final)
