from re import findall
from data_save import data_save
from os.path import relpath

def check_ip_format(ip='192.168.0.1',
                    v=4):
    try:
        *x, = ip.split('.')

        if len(x) != v:
            return False
        for a in x:
            y = int(a)
            if (y > 255) or (y < 0):
                return False
            if str(y) != a:
                return False

        return True
    except:
        return False


path = input("Путь к файлу:\n")
path += "\\" + input("Название файла:\n")

with open(path, 'r') as file:
    data = file.read()

reg = r"([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3})"
res = sorted({a for a in findall(reg, data) if check_ip_format(a)})

data_save(folder=relpath(__file__)[:-3],
                      file_format='txt',
                      wrire_mode='w',
                      data='\n'.join(res))