from math import log2
from random import randrange


def switness_test(a, r, t, N, y):
    if pow(a, t, N) == 1:
        return False
    for i in range(0, r + 1):
        x = pow(2, i) * t
        if pow(a, 2 ** i * t, N) == y:
            return False
    return True


def primality_test(N):
    r = int(round(log2(N), 0))

    s = 0
    y = t = N - 1
    while not t % 2:
        s += 1
        t //= 2

    for c in range(r):
        a = randrange(2, N)

        if switness_test(a, r, t, N, y):
            return f'{N} составное.'

    return f'{N}, вероятно простое.'


N = int(input('Число:\n'))
print(primality_test(N))
