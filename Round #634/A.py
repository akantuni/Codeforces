iter = int(input())


for i in range(iter):
    candy_num = int(input())
    if candy_num % 2 == 0:
        print(candy_num // 2 - 1)
    else:
        print(candy_num // 2)