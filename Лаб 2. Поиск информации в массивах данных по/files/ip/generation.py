from random import seed, randint, shuffle, sample
import string

def generate_alphanum_random_string(length=randint(5,20)):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(sample(letters_and_digits, length))

    return rand_string

data = []
for a in range(randint(500, 1000)):
    data.append(generate_alphanum_random_string())

for a in range(randint(500, 1000)):
    ip = []
    for b in range(randint(2, 20)):
        x = randint(-100, 1000)
        ip.append(str(x))

    ip = '.'.join(ip)
    ip = ['','.'][randint(0, 1)] + ip + ['','.'][randint(0, 1)]

    data.append(ip)

for a in range(randint(500, 1000)):
    ip = []
    for b in range(4):
        ip.append(str(randint(0, 255)))

    ip = '.'.join(ip)
    data.append(ip)

shuffle(data)

with open('IPv4.txt', 'a') as file:
    file.write('\n'.join(data))