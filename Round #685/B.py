t = int(input())

for k in range(t):
    j, q = list(map(int, input().split()))
    s = list(map(int, list(input())))
    for i in range(q):
        l, r = list(map(int, input().split()))
        l -= 1
        r -= 1
        verdict = ""
        if s[l] in s[0:l] and l != 0:
            verdict = "YES"
        elif s[r] in s[(r + 1):] and r != j - 1:
            verdict = "YES"
        else:
             verdict = "NO"

        print(verdict)
      
            
