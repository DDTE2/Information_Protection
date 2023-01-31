class prime:
    def __init__(self, N=0, k=10**4):
        self.N = N
        self.k = k
        self.little_prime = self.Sundaram()

    def Sundaram(self):
        k = self.k
        T = [True] * k
        a = int(((2*k + 1)**.5 - 1) / 2) + 1

        for i in range(1, a):
            b = (k - i) // (2 * i + 1) + 1
            for j in range(1, b):
                T[i + j + 2*i*j - 1] = False

        return frozenset(2*i+1 for i in range(1, k+1) if T[i-1])

A = prime(10**10)
print(A.little_prime)