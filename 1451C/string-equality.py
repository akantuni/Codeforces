import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    n, k = list(map(int, input().split()))
    a = input()
    b = input()

    one = [0] * 26
    two = [0] * 26

    for j in range(n):
        one[ord(a[j]) - ord("a")] += 1
        two[ord(b[j]) - ord("a")] += 1

    verdict = "Yes"
    for j in range(26):
        diff = one[j] - two[j]
        if diff < 0 or diff % k > 0:
            verdict = "No"
            break
        if j < 25:
            one[j + 1] += diff

    print(verdict)
