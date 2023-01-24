from re import findall

result = findall(fr'<img\ssrc="(.*?.gif)[;"]',
                 '<img src="http://collectionerus.ru/users/pluton/" title="мои коллекции" target="_blank" class="new_win"><img src="http://twistypuzzles.ru/forum/Themes/CurveGreen/images/www_sm.gif')
print(result)