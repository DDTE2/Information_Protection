# Поиск файлов, имеющих определенный тип
from os import walk
from os.path import relpath
from json import dumps

from data_save import data_save

path = input('Директория:\n')
string = input('Текст из файла:\n')

res = {}
errors = {}
for root,dir,files in walk(path):
    for file in files:
        for codec in ('utf-32', "utf-32be", "cp1252", "cp437", 'windows-1251', 'ascii'):
            try:
                with open(root +'\\'+ file, 'r') as text:
                    x = text.read()
                    if x.index(string) + 1:
                        if root in res:
                            res[root].append(file)
                        else:
                            res[root] = [file]
            except:
                errors[f'{root}\\{file}'] = 'Не удалось прочитать файл. Кодировка не найдена.'

if res:
    name = relpath(__file__)[:-3]
    file_format = 'json'
    data_save(name, file_format, 'w', dumps(res, sort_keys=True, indent=4, ensure_ascii=False) + '\n\n')
else:
    name = relpath(__file__)[:-3]
    file_format = 'txt'
    data_save(name, file_format, 'w', 'Ничего не найдено!\n')

if errors:
    data_save(name,file_format, 'w', dumps(errors, sort_keys=True, indent=4, ensure_ascii=False))
