from RSA import RSA_crypt

A = RSA_crypt(size=10)
print(A.private)
print(A.public)

try:
    print(A.RSA_encrypt('Проверка123б'))
except Exception as error:
    print(error)