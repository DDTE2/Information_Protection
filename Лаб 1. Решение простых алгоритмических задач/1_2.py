## Поиск файлов, имеющих определенный тип
from os import walk
from os.path import relpath
from json import dumps
from data_save import data_save

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

data_save(folder=relpath(__file__)[:-3],
          file_format='json',
          wrire_mode='w',
          data=dumps(res, sort_keys=True, indent=4, ensure_ascii=False))


