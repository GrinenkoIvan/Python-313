_str = 'I am learning Python. hello, WORLD!'  # Исходная строка.
start_range = _str.find('h')  # Находим индекс первого совпадения.
end_range = _str.rfind('h')  # Находим индекс второго совпадения.
not_reversed_part = _str[start_range + 1:end_range]  # Создаем строку из символов лежащих в найденном диапазоне.
reversed_part = ''.join(reversed(not_reversed_part))  # Разворачиваем строку
_str = _str.replace(not_reversed_part, reversed_part)  # Собираем строку путём замены подстрок.
print(_str)