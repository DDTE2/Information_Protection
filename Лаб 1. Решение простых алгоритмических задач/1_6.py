N = int(input('Число:\n'))

x = 5*N*N
x, y = (x + 4) ** 0.5, (x - 4) ** 0.5

if (int(x) == x) or (int(y) == y):
    print(f'Число {N} является числом Фиббоначи.')

    a, b = 0, 1
    l = 0
    while a <= N:
        l += 1
    ##    print(a, b)
        a, b = b, a+b

    print(f'F[{l-2}] = {a - N}')
    print(f'F[{l-1}] = {N}')
    print(f'F[{l}] = {a}')

else:
    print(f'Число {N} не является числом Фиббоначи.')
