from json import dumps

path = input("Путь к файлу:\n")
path += "\\" + input("Название файла:\n")
print(path)
separator = input("Разделитель логина и пароля:\n")

def data_read():
    global path, separator
    passwords = {}

    for enc in ('utf-32', "utf-32be", "cp1252", "cp437", 'windows-1251', 'ascii'):
        try:
            with open(path, 'r', encoding=enc) as file:
                for line in file.read().split():
                    login, password = line.split(separator)
                    if password in passwords:
                        passwords[password] += 1
                    else:
                        passwords[password] = 1
            return passwords
        except Exception as error:
            print(error, enc)

    if not passwords:
        for enc in ('utf-32', "utf-32be", "cp1252", "cp437", 'windows-1251', 'ascii'):
            try:
                with open(path, 'rb', encoding=enc) as file:
                    for line in file.read().split():
                        login, password = line.split(separator)
                        if password in passwords:
                            passwords[password] += 1
                        else:
                            passwords[password] = 1
                return passwords
            except Exception as error:
                print(error, enc)

def data_save():
    global path, separator
    passwords = data_read

    if passwords:
        data = {}
        for password in passwords:
            count = passwords[password]
            if count in data:
                data[count].add(password)
            else:
                data[count] = {password}

        data = {count:sorted(data[count]) for count in data}

        passwords.clear()
        res = ''
        for count in sorted(data):
            for password in data[count]:
                res += f'{password}: {count}\n'

        data.clear()
        print(res)