from lief import parse
from os import remove

path = input("Путь к файлу:\n") + '\\'
name = input("Название файла:\n")

with open(path + name, 'rb') as file:
    text = file.read()

with open(name + '.txt', 'wb') as file:
    file.write(text)

text = parse(name + '.txt')
with open(name + '_readed.txt', 'w') as file:
    file.write(str(text))
remove(name + '.txt')

with open(name + '___functions.txt', 'w') as file:
    for a in text.symbols:
        x = a.name
        y = a.demangled_name
        file.write(a.name + ', ' + y + '\n')
