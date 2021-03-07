t = int(input())

for i in range(t):
    ln = int(input())
    message = input()[::-1]
    paren = 0

    for char in message:
        if char == ")":
            paren += 1
        else:
            break

    if (ln - paren) < paren:
        print("Yes")
    else:
        print("No")
