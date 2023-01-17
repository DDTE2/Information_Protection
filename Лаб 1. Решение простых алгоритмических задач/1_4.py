from os import getcwd
from os.path import getsize
from os import walk

class search:
    def __init__(self, path=getcwd(), parametrs=''):
        self.path = path
        self.parametrs = parametrs.split()

        options = {}

        g = self.parametrs.index('-g')
        if g != -1:
            g += 1

        l = self.parametrs.index('-l')
        if l != -1:
            l += 1

        if self.parametrs.index('-s') + 1:
            s = True


    def min_seach(self, min_size):
        res = set()
        for root, dir, files in walk(self.path):
            for file in files:
                x = weighted_file(root, file)
                if x >= min_size:
                    res.add(x)

    def max_seach(self, max_size):
        res = set()
        for root, dir, files in walk(self.path):
            for file in files:
                x = weighted_file(root, file)
                if x <= max_size:
                    res.add(x)



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
        return self.path + self.file