from json import dumps
from data_save import data_save
from os.path import relpath

path = input("Путь к файлу:\n")
path += "\\" + input("Название файла:\n")
print(path)
separator = input("Разделитель логина и пароля:\n")

passw = {}
for codec in ('utf-32', "utf-32be", "cp1252", "cp437", 'windows-1251', 'ascii'):
    print(codec, end=';')
    try:
        with open(path, 'r', encoding=codec) as file:
            for a in file.readlines():
                login, *password = a[:-1].split(':')
                password = ':'.join(password)

                if not password in passw:
                    passw[password] += 1
                else:
                    passw[password] = 1

        break
    except Exception as error:
        print(error)

if passw:
    for codec in ('utf-32', "utf-32be", "cp1252", "cp437", 'windows-1251', 'ascii'):
        print(codec, end=';')
        try:
            with open(path, 'rb', encoding=codec) as file:
                for a in file.readlines():
                    login, *password = a.split(':')
                    password = ':'.join(password)

                    if not password in passw:
                        passw[password] += 1
                    else:
                        passw[password] = 1

            break
        except Exception as error:
            print(error)

print(passw)