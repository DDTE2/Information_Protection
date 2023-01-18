from fractions import Fraction

n = N = int(input('Число:\n'))
phi = Fraction(N)

if not n%2:
    while not n%2:
        n//=2
    phi /= 2

d = 3
while d * d <= N:
    if not n%d:
        while not n%d:
            n//=d
        phi *= d - 1
        phi /= d
    
    d+=2

if n > 1:
    phi *= n - 1
    phi //= n

print(f'φ({N}) = {phi}')


