n, k = list(map(int, input().split()))

total = 0

scores = list(map(int, input().split()))

for score in scores:
    if score > 0 and score >= scores[k - 1]:
        total += 1

print(total)
