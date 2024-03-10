line = 'I am learning Python. hello, WORLD!'
str_new_1 = line.find('h')
str_new_2 = line.rfind('h')
str_new_3 = line[str_new_1 + 1:str_new_2]
rev_new = ''.join(reversed(str_new_3))
line_new = line.replace(str_new_3, rev_new)
print(line_new)

