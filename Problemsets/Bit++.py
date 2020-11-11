n = int(input())

total = 0

for i in range(n):
    operation = input()
    if "++" in operation:
        total += 1
    elif "--" in operation:
        total -= 1

print(total)
