# Поиск файлов, имеющих определенный тип
from os import walk
from os.path import relpath
from json import dumps

path = input('Директория:\n')
name = input('Расширение файла:\n')

res = {}
for root,dir,files in walk(path):
    for file in files:
        if file.endswith(name):
            if root in res:
                res[root].append(file)
            else:
                res[root] = [file]

with open('Результаты/' + relpath(__file__)[:-3] + '.json', 'w', encoding='windows-1251') as save:
    save.write(dumps(res, sort_keys=True, indent=4, ensure_ascii=False))


