t = int(input())

for j in range(t):
    input()
    k, n, m = list(map(int, input().split()))
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    file_len = k
    check = True
    actions = []

    for i in range(len(a)):
        if a[i] > file_len:
            if len(b) > 0:
                for e in range(len(b)):
                    if b[e] > file_len:
                        l = e
                        break
                    else:
                        if b[e] == 0:
                            file_len += 1
                            actions.append(0)
                        else:
                            actions.append(b[e])
                        l = e + 1
                b = b[l:]
                if a[0] > file_len:
                    check = False
                    break
                else:
                    actions.append(a[i])

            else:
                check = False
                break
        else:
            if a[i] == 0:
                file_len += 1
                actions.append(0)
            else:
                actions.append(a[i])

    if check == False:
        print(-1)
        continue
    else:
        if len(b) > 0:
            for i in range(len(b)):
                if b[i] > file_len:
                    check = False
                else:
                    if b[i] == 0:
                        file_len += 1
                        actions.append(0)
                    else:
                        actions.append(b[i])

    if check == False:
        print(-1)
    else:
        print(" ".join(list(map(str, actions))))
