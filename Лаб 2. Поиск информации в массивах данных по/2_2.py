from urllib.request import urlopen
from re import findall
from data_save import data_save
from os.path import relpath

url = input('Сайт:\n')
with urlopen(url) as resp:
    html = resp.read().decode('utf-8')

images = set()
for a in ('png', 'jpg', 'bmp', 'gif', ''):
    reg = fr'<img\ssrc="(.*?.{a})[;"]'
    images |= set(findall(reg, html))

for a in ('png', 'jpg', 'bmp', 'gif'):
    reg = fr'<a\shref="(.*?.{a})[;"]'
    images |= set(findall(reg, html))

images = {a.split('"')[0] for a in images}
images = '\n'.join(images)

data_save(folder=relpath(__file__)[:-3],
          file_format='txt',
          wrire_mode='w',
          data=images)