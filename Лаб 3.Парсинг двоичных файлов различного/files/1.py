from lief import parse
# from lief.ELF import 
from mimetypes import guess_type
from os import remove

class bin_reader:
    def __init__(self, path, name):
        with open(path + name, 'rb') as file:
            text = file.read()

        with open(name + '.txt', 'wb') as file:
            file.write(text)

        self.text = parse(name + '.txt')
        with open(name + '_readed.txt', 'w') as file:
            file.write(str(self.text))
        remove(name + '.txt')

    def headers(self):
        if 'Class' in str(self.text.header):
            return self.headers_ELF()
        elif 'Signature' in str(self.text.header):
            self.type = 'PE'
        elif 'CPU' in str(self.text.header):
            self.type = 'Mach-O'
        else:
            self.type = None
        
    def headers_ELF(self):        
        header = {}
        text = self.text

        data = str(text.header)
        data = data.split('\n')
        for a in data:
            x,*y = a.split(':')
            if x or y:
                if y:
                    header[x] = ' '.join(y[0].split())
                else:
                    header[x] = ''
        self.type = ('ELF', header['File type'])
        return header
    def data(self):
        self.headers()
        print('Тип файла:', self.type)
        if self.type[0] == 'ELF':
            print('Точка входа:', self.headers()['Entry Point'])
            print('Смещение заголовка программы:', self.headers()['Program header offset'])
            print('Смещение заголовка раздела:', self.headers()['Section header offset'])

path = input("Путь к файлу:\n") + '\\'
name = input("Название файла:\n")

bin_file = bin_reader(path, name)
bin_file.data()
