from Crypto.PublicKey import RSA
from Crypto.Random import get_random_bytes
from Crypto.Cipher import PKCS1_OAEP, AES
from hashlib import sha256
from base64 import b64encode, b64decode
from Crypto.Util.Padding import pad, unpad
from json import dumps
from zlib import compress



class RSA_crypt:
    def __init__(self, size:int = 12,
                 public_key:bytes = b'',
                 private_key:bytes = b''):
        if not private_key:
            key = RSA.generate(2 ** size)
            self.private = key.export_key()
            self.public = key.public_key().export_key()

        else:
            self.private = private_key
            self.public = public_key

    def RSA_encrypt(self, text):
        key, text = self.AES_encrypt(text)

        chiper = PKCS1_OAEP.new(RSA.import_key(self.public))
        *text['key'], = chiper.encrypt(key)

        return my_compress(dumps(text))

    def AES_encrypt(self, text=b''):
        if isinstance(text, str):
            text = text.encode()

        key = sha256(get_random_bytes(256)).digest()
        cipher = AES.new(key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(text, AES.block_size))

        iv = b64encode(cipher.iv).decode('utf-8')
        ct = b64encode(ct_bytes).decode('utf-8')

        res = {'iv': iv, 'text': ct}
        return key, res

def my_compress(text) -> str:
    if isinstance(text, str):
        text = text.encode()
    return compress(text, 9)