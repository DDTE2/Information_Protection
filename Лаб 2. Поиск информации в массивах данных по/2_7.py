from re import sub
from json import dumps
from data_save import data_save
from os.path import relpath

path = input("Путь к файлу:\n")
path += "\\" + input("Название файла:\n")

res = {'Беларусь': [], 'Бразилия': [], 'Гонконг': [], 'Китайская Народная Республика': [], 'Колумбия': [], 'Макао': [], 'Мексика': [], 'Перу': [], 'Россия или Казахстан': [], 'США, Канада или Вест-Индия': [], 'Эквадор': [], 'Прочее': []}

with open(path, 'r') as file:
    for a in file.readlines():
        try:
            phone = a.replace('\n', '')
            phone = sub('[+()-]','' , phone)

            if set(phone) <= set('0123456789'):
                if phone.startswith('7'):
                    res['Россия или Казахстан'].append(phone)
                elif phone.startswith('1'):
                    res['США, Канада или Вест-Индия'].append(phone)
                elif phone.startswith('55'):
                    res['Бразилия'].append(phone)
                elif phone.startswith('57'):
                    res['Колумбия'].append(phone)
                elif phone.startswith('52'):
                    res['Мексика'].append(phone)
                elif phone.startswith('51'):
                    res['Перу'].append(phone)
                elif phone.startswith('593'):
                    res['Эквадор'].append(phone)
                elif phone.startswith('375'):
                    res['Беларусь'].append(phone)
                elif phone.startswith('852'):
                    res['Гонконг'].append(phone)
                elif phone.startswith('86'):
                    res['Китайская Народная Республика'].append(phone)
                elif phone.startswith('853'):
                    res['Макао'].append(phone)
                else:
                    res['Прочее'].append(phone)
        except Exception as error:
            print(phone, error, sep='; ')

countries = res.keys()
while countries:
    x, *countries = countries
    if res[x]:
        res[x].sort()
    else:
        res.pop(x)

res = dumps(res, indent=4, ensure_ascii=False)
data_save(folder=relpath(__file__)[:-3],
                      file_format='json',
                      wrire_mode='w',
                      data=res)
