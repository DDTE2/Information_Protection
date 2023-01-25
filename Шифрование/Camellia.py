MASK8 = int('0xff', 16)
MASK32 = int('0xffffffff', 16)
MASK64 = int('0xffffffffffffffff', 16)
MASK128 = int('0xffffffffffffffffffffffffffffffff', 16)
C1 = int('0xA09E667F3BCC908B', 16)
C2 = int('0xB67AE8584CAA73B2', 16)
C3 = int('0xC6EF372FE94F82BE', 16)
C4 = int('0x54FF53A5F1D36F1C', 16)
C5 = int('0x10E527FADE682D1D', 16)
C6 = int('0xB05688C2B3E6C1FD', 16)

key = '123typoiutyityiuit'
key = key.encode('windows-1251')
K = int.from_bytes(key, 'big')
if len(key) <= 128:
    KL = K
    KR = 0
elif len(key) < 256:
    KL = K >> 64
    KR = ((K & MASK64) << 64) | (~(K & MASK64))
else:
    KL = K >> 128
    KR = K & MASK128

print(KL)
print(KR)
