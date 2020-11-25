from math import sqrt

t = int(input())


def get_primes(n):
    nums = set(range(n, 1, -1))
    primes = []
    while nums:
        p = nums.pop()
        primes.append(p)
        nums.difference_update(set(range(p * 2, n + 1, p)))
    return primes


for i in range(t):
    n = int(input())
    primes = get_primes(int(sqrt(n)) + 1)
    if len(primes) == 0:
        print(1)
        print(n)
        continue
    final = []
    for prime in primes:
        if n % prime == 0:
            divisor = prime

        arr = []
        last = n
        try:

            while (last / divisor) % divisor == 0:
                arr.append(divisor)
                last = last / divisor
            arr.append(int(last))
            if len(arr) > len(final):
                final = list(map(str, sorted(arr)))
        except NameError:

            final = [str(n)]
    print(len(final))
    print(" ".join(final))
