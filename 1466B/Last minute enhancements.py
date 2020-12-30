t = int(input())

for i in range(t):
    n = int(input())
    song = list(map(int, input().split()))

    notes = set()

    for note in song:
        if note in notes:
            note += 1
        notes.add(note)
    print(len(notes))


