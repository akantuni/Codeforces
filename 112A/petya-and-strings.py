import string

alphabet = string.ascii_lowercase
str_1 = input().lower()
str_2 = input().lower()

if str_1 > str_2:
    print(1)
elif str_2 > str_1:
    print(-1)
else:
    print(0)
