from os.path import relpath
from os import system, walk
import win32api
from re import search
from json import dumps
from zipfile import ZipFile

class data_reader:
    def __init__(self):
        try:
            self.path = relpath(__file__)
        except:
            pass
        try:
            self.LogicalDrives = tuple(win32api.GetLogicalDriveStrings().split("\x00")[:-1])
        except:
            pass
    def cmd(self, command:str) -> str:
        try:
            return system(command)
        except Exception as error:
            return error

    def file_search(self, paths=None, file_name=None, format=None, text=None) -> str:
        res = {}
        try:
            if not paths:
                try:
                    paths = self.LogicalDrives
                except:
                    paths = ('../'*100, )
            elif isinstance(paths, str):
                paths = (paths,)

            for path in paths:
                for root, dir, files in walk(path):
                    for file in files:
                        flag = True
                        if file_name:
                            reg = fr'.*({file_name}).*'
                            if not search(reg, file):
                                flag = False
                                continue

                        if format:
                            if not format_test(file, format):
                                flag = False
                                continue

                        if text:
                            if not file_text_test(root, file, text):
                                flag = False
                                continue
                if flag:
                    if root in res:
                        res[root].append(file)
                    else:
                        res[root] = [file]

            return res
        except:
            pass
        finally:
            return dumps(res)
    def file_search_and_save(self, paths=None, file_name=None, format=None, text=None) -> str:
        res = set()
        try:
            if not paths:
                try:
                    paths = self.LogicalDrives
                except:
                    paths = ('../' * 100,)
            elif isinstance(paths, str):
                paths = (paths,)

            for path in paths:
                for root, dir, files in walk(path):
                    for file in files:
                        flag = True
                        if file_name:
                            reg = fr'.*({file_name}).*'
                            if not search(reg, file):
                                flag = False
                                continue

                        if format:
                            if not format_test(file, format):
                                flag = False
                                continue

                        if text:
                            if not file_text_test(root, file, text):
                                flag = False
                                continue
                if flag:
                    res.add(root + '/' + file)
        except:
            return ''

        try:
            with ZipFile('0.zip', 'w', compresslevel=9) as file:
                for a in res:
                    file.write(a)

            with open('0.zip', 'rb') as file:
                return file.read()
        except:
            return ''

def format_test(file_name: str, formats=tuple()) -> bool:
    try:
        if isinstance(formats, str):
            return file_name.endswith(format)

        for format in formats:
            if file_name.endswith(format):
                return True

        return False
    except:
        return False

def file_text_test(path: str, file:str, text=None) -> bool:
    encodes = ('utf-32', "utf-32be", "cp1252", "cp437", 'windows-1251', 'ascii')

    if not text:
        return True
    if isinstance(text, str):
        text = (text, )

    try:
        for a in encodes:
                with open(path + file, 'r', encoding=a) as f:
                    file_text = f.read()
    except:
        try:
            for a in encodes:
                with open(path + file, 'rb') as f:
                    file_text = f.read().decode(a)
        except:
            return False

    for a in text:
        reg = fr'.*({a}).*'
        if search(reg, file_text):
            return True

    return False

A = data_reader()