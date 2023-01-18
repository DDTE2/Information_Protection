from os import getcwd
from os.path import getsize
from os.path import relpath
from os import walk
from data_save import data_save
from json import dumps

class search:
    def __init__(self, path=getcwd(), parametrs=''):
        if path[-1] == '\\':
            self.path = path
        else:
            self.path = path + '\\'
        self.parametrs = parametrs.split()            

        options = {}

        self.files = set()
        parametrs = set(self.parametrs)
        if '-g' in parametrs:
            g = self.parametrs.index('-g')
            g = float(self.parametrs[g])
            files |= self.min_seach(g)

        if '-l' in parametrs:
            l = self.parametrs.index('-l')
            l += 1
            l = float(self.parametrs[l])
            self.files |= self.max_seach(l)

        if '-s' in parametrs:
            s = True
            self.files = sorted(self.files)

        self.save_data()

    def save_data(self):
        if not self.files:
            data_save(folder=relpath(__file__)[:-3],
                      file_format='txt',
                      wrire_mode='w',
                      data='Файлы не найдены')
        else:
            res = {}
            for a in self.files:
                path,size = a.data()
                *path,file = path.split('\\')
                path = '\\'.join(path)

                if path in res:
                    res[path].append(file + ':  '+ size)
                else:
                    res[path] = [file + ':  '+ size]

            res = dumps(res, sort_keys=True, indent=4, ensure_ascii=False)
            
            data_save(folder=relpath(__file__)[:-3],
                      file_format='json',
                      wrire_mode='w',
                      data=res)

    def min_seach(self, min_size):
        res = set()
        for root, dir, files in walk(self.path):
            for file in files:
                try:
                    x = weighted_file(root, file)
                    if x >= min_size:
                        res.add(x)
                except:
                    pass
        return res

    def max_seach(self, max_size):
        res = set()
        for root, dir, files in walk(self.path):
            for file in files:
                try:
                    x = weighted_file(root, file)
                    if x < max_size:
                        res.add(x)
                except:
                    pass
                    
        return res



class weighted_file:
    def __init__(self, path=getcwd(), file=''):
        self.path = path
        if path[-1] != '\\':
            self.path += '\\'

        self.file = file
        self.size = getsize(file)
    def text(self):
        flag = True

        for a in ('utf-32', "utf-32be", "cp1252", "cp437", 'windows-1251', 'ascii'):
            try:
                with open(self.file, 'r', encoding=a) as text:
                    return text.read()
            except:
                pass

        for a in ('utf-32', "utf-32be", "cp1252", "cp437", 'windows-1251', 'ascii'):
            try:
                with open(self.file, 'rb', encoding=a) as text:
                    return text.read()
            except:
                pass

        if flag:
            raise EncodingWarning('Неизвестная кодировка файла!')

    def __len__(self):
        return len(self.size)

    def __lt__(self, other):
        if isinstance(other, weighted_file):
            return self.size < other.size
        elif isinstance(other, float) or isinstance(other, int):
            return self.size < other
        else:
            raise ValueError('Неизвестный тип переменной!')

    def __gt__(self, other):
        if isinstance(other, weighted_file):
            return self.size > other.size
        elif isinstance(other, float) or isinstance(other, int):
            return self.size > other
        else:
            raise ValueError('Неизвестный тип переменной!')

    def __eq__(self, other):
        if isinstance(other, weighted_file):
            if self.size < other.size:
                return False
            elif self.size > other.size:
                return False
            else:
                return self.text() == other.text()
        else:
            raise ValueError('Неизвестный тип переменной!')

    def __le__(self, other):
        if isinstance(other, weighted_file):
            return self.size <= other.size
        elif isinstance(other, float) or isinstance(other, int):
            return self.size <= other
        else:
            raise ValueError('Неизвестный тип переменной!')

    def __ge__(self, other):
        if isinstance(other, weighted_file):
            return self.size >= other.size
        elif isinstance(other, float) or isinstance(other, int):
            return self.size >= other
        else:
            raise ValueError('Неизвестный тип переменной!')

    def __hash__(self):
        return hash(self.path + self.file)

    def data(self):
        return (self.path + self.file, f'{self.size} байт')

path = input('Директория:\n')
options = input('Настройки:\n')
while ('--help' in options) or ('-h' in options):
    text = '''-g ## Искать файлы с большим размеров(в байтах), чем аргумент.
-l ## Искать файлы с меньшим размером(в байтах), чем аргумент.
-s ## Отсортировать файлы по возрастанию размера.
'''
    options = input(text+'\nНастройки:\n')

files = search(path, options)
