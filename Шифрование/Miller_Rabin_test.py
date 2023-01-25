from math import log2, log
from random import randrange, seed
seed()


def switness_test(a, r, t, N, y):
    if pow(a, t, N) == 1:
        return False
    for i in range(0, r + 1):
        x = pow(2, i) * t
        if pow(a, 2 ** i * t, N) == y:
            return False
    return True

def primality_test(N):
    if not N % 2:
        return False
    for c in range(3, 1000, 2):
        if not N % 2:
            return False

    if (N - 1) % 6:
        if (N + 1) % 6:
            return False

    r = int(round(log2(N), 0))

    s = 0
    y = t = N - 1
    while not t % 2:
        s += 1
        t //= 2

    for c in range(r):
        a = randrange(2, N)

        if switness_test(a, r, t, N, y):
            return False

    return True

def rand_prime_number(size=10):
    while True:
        p = 6 * randrange(10 ** size, 10 ** (size + 1)) - 1

        if primality_test(p):
            x = (p - 1)//2
            if primality_test(x):
                return p

        p += 2
        if primality_test(p):
            x = (p - 1)//2
            if primality_test(x):
                return p

p = rand_prime_number(35)
try:
    x = (p).to_bytes(int(log(p,128))-2, byteorder="little")
except:
    x = (p).to_bytes(int(log(p,128))-1, byteorder="little")
print(x)
