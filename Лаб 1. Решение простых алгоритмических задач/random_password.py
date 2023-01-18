from string import ascii_letters, ascii_lowercase, digits
from datetime import datetime
from random import randint

def rand_str(min_len=5, max_len=10):
    symbols = ascii_letters + ascii_lowercase + digits

    res = ''    
    for c in randint(min_len, max_len):
        res += symbols[randint(0, len(symbols) - 1)]

    return res        

with open(path +
          datetime.utcnow().strftime('%d-%m-%Y %H_%M_%S') +
          '.csv', 'w') as file:
    file.write(f'{rand_str()}:{rand_str()}\n')
