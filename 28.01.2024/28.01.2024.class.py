# Рекурсия ------------------------------------------------------

# def elevator(n):  #попадает введённое число n1
#     if n == 0:
#         print("Вы в подвале")
#         return    # останавливает вызов ( n - 1)
#     print("=>", n)  # выводит от 10 9 8 7 6 5 4 3 2 1
#     elevator(n - 1)
#     print(n, end=" ")  # выводит знвчения в обратном порядке 1 2 3 4 5 6 7 8 9 10
#
#
# n1 = int(input("На каком ввы этаже: "))  # вводим цифру 10
# elevator(n1)

# -------------------------------------------------------------------------------------

# решение задачи с помощью функции
# def sum_list(lst):
#     res = 0
#     for i in lst:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25

# та же задача только при помощи рекурсии

# def sum_list(lst):  # [1, [3, [5, [7, [9] с каждым вызовом lst уменьшается на [0] индекс
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])  # 1+3+5+7+9
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25

# --------------------------------------------------------------------------------------

# def to_str(n, base):  # n = 365
#     convert = "0123456789ABCDEF"
#     if n < base:  # n(365) < base(10)
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# # print(to_str(365, 10))  # 365
# # print(to_str(365, 2))  # 101101101
# # print(to_str(365, 8))  # 555
# # print(to_str(365, 16)) # 16D
# print(to_str(254, 16))  # FE

# --------------------------------------------------------------------------------------

# names = ['Adam', ['Bob', ['Chet', 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
# print(names)
#
#
# # print(names[0])
# # print(isinstance(names[0], list))
# # print(names[1])
# # print(isinstance(names[1], list))
# # print(names[1][1])
# # print(isinstance(names[1][1], list))
# # print(names[1][1][0])
# def count_item(lst):
#     count = 0
#     for item in lst:
#         if isinstance(item, list):
#             count += count_item(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_item(names))

# -----------------------------------------------------------------------------------------------

# удаление пробелов и табуляции из строки
# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove(" Hello\tWorld "))

# -------------------------------------------------------------------------------------------------

# Работа с файлами
# txt
# binary

# f = open(r'D:\PyCharm.Progect\text.txt', mode='r') # абсолютный путь
# # f = open('text.txt', 'r')  # относительный путь
# print(*f) # распаковка файла
# print(f)
# print(f.closed) # False
# f.close() # Закрытие файла
# print(f.closed) # True
# print(f.mode) # r
# print(f.name) # D:\PyCharm.Progect\text.txt / text.txt
# print(f.encoding) # cp1251

# -------------------------------------------------------------------------------------------------

# f = open('text313.txt', 'r')
# # print(f.read(3)) #  считывает указанное количество символов
# # print(f.read()) # считывает полностью из файла
# print(f.readline()) # считывает полностью строку до переноса(/n)
# print(f.readline())
# f.close()

# -------------------------------------------------------------------------------------------------

# f = open('text313.txt', 'r')
# print(f.readlines(16)) # считывает списков всех строк
# print(f.readlines())
# f.close()

# -------------------------------------------------------------------------------------------------

# f = open('text313.txt', 'r')
# for line in f:
#     print(line)
# f.close()

#--------------------------------------------------------------------------------------------------
# # вывести количество строк в файле
# f = open('text313.txt', 'r')
# count = 0
# for line in f:
#     print(line)
#     count += 1
# f.close()
# print("count = ", count)
# или вариант 2 ------------------------------------------------------
# f = open('text313.txt', 'r')
# print("count = ", len(f.readlines()))
# f.close()

# --------------------------------------------------------------------------------------------------

# f = open("xyz.txt", "w") # 'w' - создание файла и очищает если что то записано
# f.write("Hello\nWorld!\n") # записываем данные
# f.close()
# f = open("xyz.txt", "a") # 'a' - дописывает данные в конец текста
# f.write("Next new text.\n") # write - функция записи в файл
# f.close()

# -------------------------------------------------------------------------

# f = open("xyz.txt", "w")
# line = ['This is line 1\n', 'This is line 2']
# f.writelines(line)
# f.close()




