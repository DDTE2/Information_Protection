from urllib.request import urlopen
from json import load, dumps
from re import sub

def phone_validate(phone):
    global data

    phone = phone.replace('\n', '')
    getInfo = "https://htmlweb.ru/geo/api.php?json&telcod=" + phone

    try:
        infoPhone = urlopen( getInfo )
        country = load(infoPhone)
        if 'error' in country:
            return phone, country['error']

        country = country['country']['fullname']

        if country in data:

            phone = sub('[+()-]','' , phone)
            data[country].add(phone)

            return phone, country
    except Exception as error:
        return phone, error

path = input("Путь к файлу:\n")
path += "\\" + input("Название файла:\n")

data = {}
with open(path, 'r') as file:
    for phone in file.readlines():
        print(phone_validate(phone))

print(dumps(data, sort_keys=True, indent=4, ensure_ascii=False))