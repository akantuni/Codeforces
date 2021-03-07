t = int(input())

for i in range(t):
    seq = list(input())

    if seq.index(")") != 0 and seq.index("(") != len(seq) - 1:
        if "".join(seq).count("?") % 2 == 0:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
