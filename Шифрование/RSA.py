from Crypto.PublicKey import RSA

key = RSA.generate(2**13)
with open('private.txt', 'wb') as file:
    file.write(key.export_key())
with open('public.txt', 'wb') as file:
    file.write(key.publickey().export_key())
