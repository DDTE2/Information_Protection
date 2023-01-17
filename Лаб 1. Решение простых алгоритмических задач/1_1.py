# Поиск файла
from os import walk
from os.path import relpath
from json import dumps

path = input('Директория:\n')
name = input('Название файла:\n')

with open('Результаты/' + relpath(__file__)[:-3] + '.txt', 'w', encoding='windows-1251') as save:
    for root,dir,files in walk(path):
        for file in files:
            if file == name:
                save.write(root + '\n')

