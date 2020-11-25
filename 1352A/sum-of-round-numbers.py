t = int(input())

for i in range(t):
    adds = []
    t = input()
    appends = 0
    for idx, num in enumerate(t):
        if int(num) != 0:
            appends += 1
            adds.append(str(num) + str("0" * (len(t) - idx - 1)))
    print(appends)
    print(" ".join(adds))
