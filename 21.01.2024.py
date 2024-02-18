import re

data = '123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru'
pattern = r'[.\-\w]+@[.\w]+'
print(re.findall(pattern, data))


