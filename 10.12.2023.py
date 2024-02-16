check_shape = tuple(input("Введите по порядку, без пробелов, элементы кортежа: "))
print(check_shape)
lst = list(check_shape)
new_shape = []
for i in range(len(lst)):
    if i in lst:
        lst.append(i)
for i in lst:
    if i not in new_shape:
        new_shape.append(i)
for i in new_shape:
    print("Количество", i, "=", int(check_shape.count(i)))
