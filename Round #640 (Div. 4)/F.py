t = int(input())

for i in range(t):
    nums = input().split()
    n0 = int(nums[0])
    n1 = int(nums[1])
    n2 = int(nums[2])

    str = ''
    zeroone = 0


    if n2 > 0:
        str += '1' * (n2 + 1)

    if n0 > 0:
        str += '0' * (n0 + 1)
        zeroone += 1

    if n1 == 1:
        pass

    else:
        while zeroone < n1:
            if str[-1] == '0':
                str += '1'
            elif str[-1] == '1':
                str += '0'
            zeroone += 1

    print(str)