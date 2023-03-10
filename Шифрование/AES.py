import json
from base64 import b64encode, b64decode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from hashlib import sha256
from zlib import compress

def my_compress(text) -> str:
    if isinstance(text, str):
        text = text.encode()
    return compress(text, 9)

class crypt:
    def __init__(self, password='', text=''):
        self.key = sha256(password.encode()).digest()
        self.text = text
    def encrypt(self):
        text = my_compress(self.text.encode())
        cipher = AES.new(self.key, AES.MODE_CBC)
        ct_bytes = cipher.encrypt(pad(text, AES.block_size))

        iv = b64encode(cipher.iv).decode('utf-8')
        ct = b64encode(ct_bytes).decode('utf-8')

        res = json.dumps({'iv':iv, 'text':ct})
        return my_compress(res)
    
    def decrypt(self):
        b64 = json.loads(self.text)
        iv = b64decode(b64['iv'])
        ct = b64decode(b64['text'])
        cipher = AES.new(self.key, AES.MODE_CBC, iv)

        self.text = unpad(cipher.decrypt(ct), AES.block_size).decode()
        return self.text
