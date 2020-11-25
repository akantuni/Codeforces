t = int(input())

for i in range(t):
    n = int(input())
    bids = list(map(int, input().split()))

    if len(bids) == 1:
        print(bids[0])
        continue
    bids_sorted = sorted(bids)

    for i in range(len(bids_sorted)):
        if i == len(bids_sorted) - 1:
            if bids_sorted[i] != bids_sorted[i - 1]:
                print(bids.index(bids_sorted[i]) + 1)
                break
            else:
                print(-1)
                break

        elif bids_sorted[i - 1] == bids_sorted[i]:
            continue
        else:
            if bids_sorted[i] != bids_sorted[i + 1]:
                print(bids.index(bids_sorted[i]) + 1)
                break
