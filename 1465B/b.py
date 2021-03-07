from math import gcd
import sys

input = sys.stdin.readline


def lcm(array):
    running = array[0]
    for i in range(1, len(array)):
        running = abs(array[i] * running) // gcd(array[i], running)
    return running


def find_fair_num(num):
    arr = sorted(list(map(int, list(str(num)))))
    final_ind = -1
    for i, char in enumerate(arr):
        if char == 0:
            final_ind = i
        else:
            break
    if final_ind > -1:
        arr = arr[final_ind + 1 :]
    if num % lcm(arr) == 0:
        print(num)
    else:
        find_fair_num(num + 1)


t = int(input())

for i in range(t):
    num = int(input())
    find_fair_num(num)
