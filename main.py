# print("Hello,", name)
# import random


# age = 20.4
# print(age)
# text = "Hello"
# print(text)
# print(text + str(age))
# print(type(age))  # числовое значение int - 20, float 20.4
# print(type(text))  # str - "Hello"
# a = False
# print(a)
# print(type(a))  # bool - True, False
# a = 4
# b = 5
# print(a, id(a))
# print(b, id(b))
# a = b
# print(a,id(a))
# print(b, id(b))

# a = b = c = 1
# print(a)
# print(b)
# print(c)

# a, b, c = 5, "Hello", 9.2
# print(a)
# print(b)
# print(c)

# name5 = "Igor"  # цифра вначале False
# name_new = "Ihor"  # нижнее подчёркивание True
#
# print(name5)
# print(name_new)

# PI = 3.14
# print(PI)
# PI = 2
# print(PI)

# a = 1
# b = 2
# print("a:", a)
# print("b:", b)
#
# # c = a
# # a = b
# # b = c
# a, b = b, a
# print("a:", a)
# print("b:", b)

# print("строка символов")
# print('строка символов D:\\folder\\file.txt')

# s1 = "Hello"
# s2 = "Rython"
# s3 = s1 + ", " + s2 + "!\t\t")
# # print(s1, ", ", s2, "!")
# b = (s3 * 5)
# print(b)
# print(6 + 2)

# print(6 - 2)
# print(6 * 2)
# print(6 / 2)
# print(6 // 2)
# print(6 / 4)
# print(6 // 4)  # целочисленное деление
# print(6 ** 2)
# print(6 % 4)  # остаток от деления


# Домашняя работа от 11.11.2023

# a = 5
# b = 7
# c = 3
# print("Сумма чисел:", a + b + c)
# print("Произведение чисел:", a * b * c)
# print("Среднее арифметическое:", (a + b + c) / 3)


# ______________Классная работа от 12.11.2023______________________________#

# num = 4321
# print("Исходное число :", num)
# res = num % 10 * 1000
# num //= 10
# res = num % 10 * 100
# num //= 10
# res = num % 10 * 10
# num //= 10
# res = num % 10 * 10
# num //= 10
# res += num % 10
# print(res)  # разобрать при просмотре

# num1 = "2.3"
# num2 = 3
# # res = num1 + str(num2)  # 23
# # res = int(num1) + num2
# res = float(num1) + num2
# print(res)

# print(int(3.8))
# print(round(3.891, 3))  # вторая цифра определяет колличество чисел после запятой
# print(type(round(3.891, 2)))

# name = "Виктор"
# age = 28
# print("Меня зовут ", name, ". Мне", age, "лет.", end=" ", sep=" & ")
# print("Я учу Python")

# Задача(пользователь вводит два числа)
#
# name = input("Введите имя: ")
# print(name)

# num = int(input("Введите число: "))
# power = int(input("Введите степень: "))
# # num = int(num)
# res = int(num) ** int(power)
# print("Число", num, "В степени", power, "равно", res)
# print(type(num))

# b1 = True
# b2 = False
# print(b1 + 5)
# print(b2 + 5)

# False =>

# print(bool("python"))
# print(bool(""))
# print(bool(5))
# print(bool(0))
# print(bool(False))

# print(7 == 7)  # True
# print(7 == "7")  # False
# print(7 != 10 - 7)
# print(2 < 4 >= 5)  # Один из False, то на выходе будет False

# a = 10
# b = 5
# c = a == b
# print(a, b, c)

# print(5 - 3 == 2 and 1 + 3 == 4)
# print(5 - 3 == 2 and 1 + 3 < 4)


# print(5 - 3 == 2 or 1 + 3 == 4)  # True
# print(5 - 3 == 2 or 1 + 3 < 4)  # True
# print(5 - 3 > 2 or 1 + 3 == 4)  # True
# print(5 - 3 > 2 or 1 + 3 < 4)  # False

# print(9 - 7)
# print(not 9 - 7)
# print(not 9 - 9)

# cnt = 5
# if cnt < 10:
#     cnt += 2
#     print(cnt)

# age = int(input(("Введите свой возраст: ")))
# if age >= 18:
#     print("Доступ на сайт разрешён")
# else:
#     print("Доступ запрещён")

# a = 35
# b = 25
# if a > b:
#     print("a > b")
# elif a < b:
#     print("a < b")
# else:
#     print("a == b")

# Задача # ----------------------------------------------------------------

# a = input("Введите первую сторону треугольника: ")
# b = input("Введите вторую сторону треугольника: ")
# c = input("Введите третью сторону треугольника: ")
#
# if a == b == c:
#     print('Треугольник равносторонний.')
# elif (a == b != c) or (a == c != b) or (b == c != a):
#     print('Треугольник равнобедренный.')
# else:
#     print('Треуголник разносторонний.')

# ----------------------------------------------------------------

# day = int(input("Введите день недели цифрой: "))
# if 1 <= day <= 5:  # (day >= 1) and (day <= 5):
#     print("Рабочий день - ", end="")
# if day == 1:
#     print("понедельник")
# if day == 2:
#         print("вторник")
# if day == 3:
#         print("среда")
# if day == 4:
#         print("четверг")
# if day == 5:
#         print("пятница")
# elif day == 6 or day == 7:
#     print("Выходной день - ")
# if day == 6:
#         print("суббота")
# if day == 7:
#             print("воскресенье")
# else:
#     print("Такого дня недели нет")  # пересмотреть и исправить

# ----------------------------------------------------------------

# Домашняя работа от 12.11.2023 -- Пользователь вводит число/ программа выводит время года и месяц  #

# month = int(input("Введите месяц года (цифрой): "))
# if 1 <= month <= 2 or month == 12:
#     print("Это зима: ")
#     if month == 1:
#         print("Январь!")
#     if month == 2:
#         print("Февраль!")
#     if month == 12:
#         print("Декабрь!")
# elif month == 3 or month == 4 or month == 5:
#     print("Это весна: ")
#     if month == 3:
#         print("Март!")
#     if month == 4:
#         print("Апрель!")
#     if month == 5:
#         print("Май!")
# elif month == 6 or month == 7 or month == 8:
#     print("Это лето: ")
#     if month == 6:
#         print("Июнь!")
#     if month == 7:
#         print("Июль!")
#     if month == 8:
#         print("Август!")
# elif month == 9 or month == 10 or month == 11:
#     print("Это осень: ")
#     if month == 9:
#         print("Сентябрь!")
#     if month == 10:
#         print("Октябрь!")
#     if month == 11:
#         print("Ноябрь!")
# else:
#     print("Такого месяца ещё не придумали.")

# ----------------------------------------------------------------

# anything = input("Tell me anything...")
# print("Hmm...", anything, "...Really?")

# leg_a = float(input("Enter the length of the first side: "))
# leg_b = float(input("Enter the length of the second side: "))
# print("Hypotenuse length is " + str((leg_a**2 + leg_b**2) ** .5))

# name = input("Enter your name: ")
# print("Hello, " + name + ". Nice to meet you!")
# print("\nPress Enter to end the program.")
# input()
# print("THE END.")

# ------------ 18.11.2023 ----------------#

#    Классная работа     #


# n = int(input("Введите количество ворон: "))
# if <= 0 <= 9:
#     print("На ветке", n, end=" ")
#     if n == 1:
#         print("ворона")
#     elif 2<= n <= 4:  # n == 2 or n == 3 or n == 4
#         print("вороны")
#     else:
#         print("ворон")
# else:
#     print("Ошибка ввода данных")  # программа работает #

# ----------------------------------------------------------------

# password = "qwerty"
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case "user":
#         print("Пользователь")
#     case _:
#         print("Логин не найден")

# ----------------------------------------------------------------

# day = 'вторник'
# time = 14
# match day:
#     case "понедельник" | "вторник" | "среда" | "четверг" | "пятница" if 9 <= time <= 13 or 15 <= time <= 16 :
#         print("Рабочий день")
#     case "суббота" | "воскресенье":
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")

# ----------------------------------------------------------------

# a, b =  20, 30
#
# print(a if a < b else b)

# ----------------------------------------------------------------

# a, b = 20, 30
#
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# ----------------------------------------------------------------

# a = 5
# b = 0
# print("на ноль делить нельзя " if b == 0 else a / b)
# print(a / b)

# ----------------------------------------------------------------

# try:
#     n = int(input("Ввести целое число: "))
#     print(n * 2)
#
# except ValueError:
#     print("Что то пошло не так")
#
# print("перешли на следующую строку")

# ----------------------------------------------------------------

# n = input(" введите №")
# m = input(" введите №")
#
# try:
#     n = int(n)  #
#     m = int(m)
# except ValueError:
#     n = str(n)
# finally:
#     print(n + m)

#  циклы # ----------------------------------------------------------------

# i = 0
# while i < 5:
#     print("i =", i)
#     i+=1

# ----------------------------------------------------------------

# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1

# ----------------------------------------------------------------

# i = 0
# while i <= 20:
#     print("i ", i)
#     i += 2

# ----------------------------------------------------------------

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#         i += 1

# ----------------------------------------------------------------

# n = int(input("Количество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# ----------------------------------------------------------------

# n = int(input("Лоличество символов: "))
# print("*\n" * n)

# ----------------------------------------------------------------

# a = int(input("Ввести начало диапазона: "))
# b = int(input("Ввести конец диапазона: "))
# res = 0
# while a <= b:
#     if a % 2 != 0:
#         res += a
#     a += 1
# print(res)

# ----------------------------------------------------------------

# Домашняя работа #
# n = int(input("Введите кол-во символов: "))
# symbol = input("Тип символа")
# orient = int(input("0- горизонт\n1- вертикаль\nориентация линии"))
# i = 0
# while i < n:
#     if orient == 0:
#         print(symbol, end=" ")
#     if orient == 1:
#         print(symbol)
#     i += 1


# ----------------------------------------------------------------
# 19.11.2023

# n = input("Введите целое число: ")
#
# while type(n) != int and type(n) != float:
#     try:
#         if n // 1 == 0:
#             print("Чётное")
#     except ValueError:
#         print("Число не целое")
#     n = input("Введите целое число: ")
#     finally:
#         print("Программа завершена", n)

# if n % 2 == 0:
#     print("Чётное")
# else:
#     print("Нечётное") # не работает

# ----------------------------------------------------------------

# i = 0
# while i < 10:
#     if i == 3:
#         i += 1
#         continue
#     print(i, end=" ")
#     if i == 5:
#         break
#     i += 1
# print(("\nЦикл завершён"))

# i = 0
# while True:
#     print(i)
#     if i == 5:
#        break
#     i += 1
#

# ----------------------------------------------------------------

# Домашняя работа от 19.11.2023
# start = 1
# while True:
#     n = int(input("Угадайте число от 1 до 100: "))
#     number = 51
#     if n < number:
#         print("Ваше предположение меньше, чем число.")
#     if n > number:
#         print("Ваше предположение больше, чем число.")
#     if n == 0:
#         print("Ноль это условие выхода из программы , программа завершена .")
#         break
#     elif n == number:
#         print("Вы угадали загаданное число: ", number)
#         break
#     start += 1
# print("Количество попыток =", start)

# ----------------------------------------------------------------

# i = 0
# while i < 10:
#     if i == 5:
#         break  # останавливает цикл
#     print(i, end=" ")
#     i += 1
# else:
#     print("\nЦикл окончен. i =", i)  # работает

# ----------------------------------------------------------------

# таблица умножения
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print(i, "*", j, "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1  # программа работает

# ----------------------------------------------------------------

# i = 0
# while i < 5:
#     j = 0
#     while j < 16:
#         if j % 2 == 0:
#             print("*", end="")
#         else:
#             print("&", end="")
#         j += 1
#     print()
#     i += 1  #  работает

# i = 0
# while i < 5:
#      j = 6
#     if i % 2 == 0:
#         print("+" * 3)
#     else:
#         print("-" * 4)
#     i += 1

# i = 0
# while i < 5:
#     j = 0
#     while j < i:
#         print(" ", end="")
#         j += 1
#     print("*")
#     i += 1  #  работает

# for i in "Hello!", "World!":
#     print(i)

# for i in range(10, 0, -2):
#     print(i, end=" ")
#
# print()
#
# i = 0
# while i < 10:
#     print(i, end=" ")
#     i += 1

# a = int(input("Ведите целое число: 100"))
# for i in range(11, a):
#     if a % 10 == i // 100:
#             print(i, end=" ")  #  перепроверить и решить


#  02.12.2023____------------------
# a = [1, 2, 3]
# b = a.copy()
# print("a =",a)
# print("b =",b)
#
# a.append(20)
# print("a =",a)
# print("b =",b)
# b.append(120)


# a = [5, 4, 1, 2, 3]
# print(a)
# # a.reverse()
# # print(a)
#
# # a.sort()
# # print(a)
# a.sort(reverse=True)
# print(a)


# b =["Виталий","Сергей","Александр","Анна"]
# b.sort(key=len, reverse=True)
# print(b)

# a = [5, 4, 1, 2, 3]
# print(a)
# a.sort()
# print(a)

# sort = sorted(a)
# print(sort)

#  Генерация случайных данных  ----->----------->-------------->------------->------------->


# print(random.random())
# print(random.randint(3, 9))
# print(random.randrange(3, 9))
#
# print(round(random.uniform(10.5, 25.5), 2))

# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(random.choice(city_list))
# print(random.choices(city_list, k=3))
# random.shuffle(city_list)
# print(city_list)


# s = [55, 66, 77, 88, 99, 9, 8, 7, 6, 5, 4, 1, 2, 3]
# print(random.choice(s))
# print(random.choices(s, k=5))

# lst = [5, 4, 3, 2, 1]
# print(len(lst))
# print(sum(lst))
# print(min(lst))
# print(max(lst))

# Задача --------------------------------

# import random
# mas = [random.randint(0, 20) for i in range(10)]
# print(mas)

# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# mas_ = max(mas)
# print(mas_)
# mas.remove(mas_)
# mas.insert(0, mas_)
# print(mas)  #  вариант 1 программа работает

# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# max_ = max(mas)
# print(max_)
# mas.remove(max_)
# mas.insert(0, max_)
# print(mas)    # вариант 2 программа работает

#  Перемена--------------------------------
# Задача : программа находит мин значение и выводит в новый список с удалением других объектов впереди себя
# import random
#
# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
#
# min_ch = min(lst)
# print("min =", min_ch)
#
# ind_min = lst.index(min_ch)
# print("index min =", ind_min)
#
# del lst[: ind_min]
# print(lst)
# print(lst(ind_min))  # перепроверить

# lst = [5]
# print(lst)
# if not lst:
#     print("Список пуст")
# else:
#     print("В списке есть элементы")

# import random
#
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
#
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print("Третий список: ", c)
# d = []
# for element in a:
#     if element not in d:
#         d.append(element)
# for element in b:
#     if element not in d:
#         d.append(element)
# print("Элементы обоих списков без повторений: ", d)
# c = []
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print("Элементы общие для обоих списков: ", c)

# c = [min(a), min(b), max(a), max(b)]
# print(c)    # задача работает

#  ----- Домашняя работа от 02,12,2023


# import random
#
# print(random.sample(range(1, 10+1), 10))

# a = [random.randint(0, 10) for i in range(10)]
# b = []
# for element in a:
#     if element not in b:
#         b.append(element)
# print(b)

# import random
#   a = [random.randint(1, 10) for i in range(10)]
# for v in range(1, 10):
#     v = 2 ** v
#     b = list(random_range(v))
#     print("Need", v, "found", len(set(b)), "(min,max)", (min(b), max(b)))
# print("", b)
# print()

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# # m = ["Hello", "World"]
# print(m)
# # print(len(m))
# # print(m[1][2])
# print()
# # for row in range(len(m)):
# #     for col in range(len[row]):
# #         print(m[row][col], end="\t")
# #         print()
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()

# 3.12.2023-----------------------------------------------------------

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# print(matrix)


# import random
# w, h = 3, 4
# col_vo = 0
# matrix = [[random.randint(-10, 20) for x in range(w)]for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#         if x < 0:
#             col_vo += 1
#         print(col_vo)
#     print()               #работает но подделать


# for x, y in [[1, 2], [3, 4], [5, 6], [7, 8]]:
#     print(x, "+", y, "=", x + y)


# import random
#
# w, h = 3, 4
# matrix = [[input("->") for x in range(w)] for y in range(h)]
# for row in matrix:
#     for x in row:
#         print(x, end="\t")
#     print()

# import math
#
# num1 = math.sqrt(4)
# num2 = math.ceil(3.1)   # округляет в большую сторону
# num3 = math.floor(3.8)   # округляет в меньшую сторону
#
# print(num1)
# print(num2)
# print(num3)
#
# print(math.pi)

# import math as m
#
#
# num1 = m.sqrt(4)
#
# print(num1)

# import time
# import locale

# locale.setlocale(locale.LC_ALL, "ru")
# seconds = time.time()
# print("Количество секунд: ", seconds)
#
# local_time = time.ctime(1201589052)
# print("Местное время: ", local_time)
#
# res = time.localtime()
# print(res)
# print(res.tm_year)
#
# # print(time.strftime("Today is %B %d, %Y"))
# print(time.strftime("Сегодня:  %B %d, %Y"))
# print(time.strftime("%d/%m/%Y, %H:%M:%S", time.localtime()))
# start = time.monotonic()
# time.sleep(5)
# finish = time.monotonic()
# res = finish - start
# print(res)

# Функция-------------------------------------------

# print()
#
#
# def hello(name):
#     print("Hello,", name)
#
#
# print("Irina")
# print("Igor")

# def get_sum(a, b):
#     print(a + b)
#
#
# x = 2
# y = 5
# get_sum(x, y)
# get_sum("abc", "def")


# def symbol(count, a, b):
#     for i in range(count):
#         if i % 2 == 0:
#             print(a, end="")
#         else:
#             print(b, end="")
#     print()
#
#
# symbol(9, '+', '-')
# symbol(7, 'x', 'y')


# def get_sum(a, b):
#     print("Сумма:", end="")
#     return a + b
#
# x = 2
# y = 5
# res = get_sum(x, y)
# print(res)

# def maximum(one, two):
#     if one > two:
#         return one
#     else:
#         return two
#
#
# print(maximum(9, 16))


# def maximum(one, two):
#     if one > two:
#         return one - two
#     else:
#         return two + one
#
#
# print(maximum(8, 9))


# def cube(a):
#     return a ** 3   # a * a * a
#
#
# for i in range(1, 11):
#     print(i, "в кубе =", cube(i))

# def change(lst):
#     print(lst)
#     symbol = lst.pop(0)
#     lst.append(symbol)
#     return lst
#
#
#
# print(change([1,2,3]))    # дописать 12:30 и далее задача

# def is_greater(x, y):
#     if x > y:
#         return True
#     else: return False
#
#
# a = 10
# b = 5
#
# print(is_greater(a, b))
# print(is_greater(5, 10))
#
# if is_greater(a, b):
#     print(a, "больше", b)
# else:
#     print(b, "больше", a)
#


# def check_password(password):
#     has_upper = False
#     has_Lower = False
#     has_num = False
#
#
#     for ch in password:
#         if "A" <= ch <= "Z":
#             has_upper = True
#         elif 'a' <= ch <= 'z':
#             has_Lower = True
#         elif '0' <= ch <= '9':
#             has_num = True
#
#
#     if len(password) >= 8 and has_upper:
#         return True
#     return False
#
#
# p = input("Введите пароль: ")
# if check_password(p):
#     print("Это надёжный пароль")
# else:
#     print("Это ненадёжный пароль")  # работает

# print(random.sample(range(0, 10), 10))

# 09.12.2023 --------------------------------------------------------------

# def get_sum(a, b, c=0, d=1):
#      return a + b + c + d
#
# print(get_sum(1, 5, 2, 7))
# print(get_sum(1, 5, 2))
# print(get_sum(1, 5))
# print(get_sum(1, 5, d=2))
# n1 = 1
# n2 = 5
# n4 = 2
# print(get_sum(n1, n2, d=n4))

# def set_param(c=20, s="-"):
#     print(s * c)
#
#
# set_param()
# set_param(7)
# set_param (30, "*")
# set_param (s="*")

# def digit_sum(n, even=True):
#     s = 0
#     while n > 0:
#         current = n % 10
#         if even and current % 2 == 0:
#             s += current
#         if not even and current % 2:  # или elif тоже можно
#             s += current
#         n //= 10
#     return s
#
# print("Сумма четных цифр:")
# print(digit_sum(9874023))
# print(digit_sum(38271))
# print(digit_sum(123456789))
# print("\nСумма нечетных цифр:")
# print(digit_sum(9874023, even=False))
# print(digit_sum(38271, even=False))
# print(digit_sum(123456789, even=False))


# def display_info(name, age):
#     print("Name:", name, "\nAge", age)
#
#
# display_info("Ira", 23)
# display_info(23, "Ira")
# display_info(age=23, name="Ira")

# Изменяемые и неизменяемые объекты

# lt1 = [1, 2, 3]
# lt2 = [1, 2, 3]
# print(id(lt1))
# print(id(lt2))
# print(lt1 == lt2) # True
# print(lt1 is lt2) # False

# n = 5
# m = 5
# print(n == m)
# print(n is m)


#  Кортеж (tuple) --------------------------------------------------------

# lst = [10, 20, 30]
# tpl = (10, 20, 30)
# print(lst.__sizeof__())
# print(tpl.__sizeof__())
#
# a = (5,)  # 5, символизируют кортежу
# print(type(a))
# # b = tuple()
# # print(type(b))
# print(a)
# # print(b)


# n = [1, 2, 3]
# b = tuple(("Hello", "Python"))
# print(type(b))
# print(b)

# from random import randint
#
# s = tuple(input("-> ") for i in range(5))
# print(s)
# s = tuple(int(input("-> ")) for i in range(5))
# print(s)
# s = tuple(randint(0, 100) for i in range(5))
# print(s)

# ------------------------------------------------------------------------------

# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# ------------------------------------------------------------------------------

# t1 = tuple("Hello")
# t2 = tuple("world")
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t3.count('l')) # считает количество элементов в кортеже
# if 'e' in t3:
#     print(t3.index('e')) # index возвращает 1й индекс данного элемента
#                            ('e', 4)
#
# for i in t3:
#     print(i, end="")

# задача-----------------------------------------------------------------------------

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#         # a = tpl.index(el)
#         # b = tpl.index(el, a+1)
#         # return tpl[a:b+1]      или .....
#             return tpl[tpl.index(el):tpl.index(el, tpl.index(el) + 1) + 1]
#         else:
#             return tpl[tpl.index(el):] # возвращает по индексу элемента и до конца
#
#     else:
#         return tuple()
#
# print(slicer((1, 2, 3, 4, 2), 2)) # (2, 3, 4, 2)
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2, 3), 3)) # (3, 4, 8, 8, 9, 2, 3)
# print(slicer((1, 2, 8, 5, 1, 2, 9), 1)) # (1, 2, 8, 5, 1)

# --------------------------------------------------------------------------------------

# t = (10, 11, [1, 2, 3], [4, 5, 6], ['hello', 'world'])
# print(t, id(t))
# t[4][0] = "new"
# t[4].append("hi")
# print(t, id(t))

# t = (1, 2, 3)
# x = t[0]
# y = t[1]
# z = t[2]
# #   или x, y, z = t   распаковка кортежа
# print(x, y, z)

# ------------------------------------------------------------------------------

# def get_user():
#     name = "Tom"
#     age = 22
#     is_married = False
#     return name, age, is_married
#
#
# first, year, setr = get_user()
#
# print(first, year, setr)


# import random
# initial = tuple([random.randint(0, 5) for _ in range(10)])
# print(initial)
# other = tuple([random.randint(-5, 0) for _ in range(10)])
# print(other)
# upshot = initial + other
# print(upshot)
# print("0 = ", upshot.count(0))


# 10.12.2023 --------------------------------------------------------------------

# tpl = (1, 2, 3, 4, 5, 6)
# print(tpl)
# lst = list(tpl)
# print(lst)
# ptl1 = tuple(lst)
# print(ptl1)
# del ptl1
# print(ptl1)

# countries = (
#     ("Германия", 80.2, (("Берлин", 3.326), ("Гамбург", 1.718))),  # Распаковка кортежей
#     ("Франция", 66, (("Париж", 2.2), ("Марсель", 1.6)))
# )
# print(countries, end="\n\n")
#
# for country in countries:
#     country_name, country_population, cities = country
#     print("\nСтрана:", country_name, "Населенние =", country_population)
#     for city in cities:
#         city_name, city_population = city
#         print("\tГород", city_name, "Город", city_population)


# ---------- Домашняя работа от 09.12.2023, случайные списки кортежа от 0 до 5 и от -5 до 0,
# сложить оба картежа и вывести в ответ сколько выпадает случайных чисел 0.-------------------
# Вариант
# import random
#
# def funk():
#
# initial = tuple([random.randint(0, 5) for _ in range(10)])
# print(initial)
# other = tuple([random.randint(-5, 0) for _ in range(10)])
# print(other)
# upshot = initial + other
# print(upshot)
# print("0 = ", upshot.count(0))

# Вариант 2 через функцию----------------------------------
# from random import randint
#
#
# def create_tuple(start: int, end: int) -> tuple:
#     return tuple(randint(start, end) for _ in range(10))
#
#
# tpl1 = create_tuple(0, 5)
# tpl2 = create_tuple(-5, 0)
# tpl3 = tpl1 + tpl2
#
# print(tpl1, tpl2, tpl3, '0 = ' + str(tpl3.count(0)), sep='\n')


# -------------Домашняя работа от 10.12.2023 , вывести статистику чачтотности чисел в кортеже----
# Вариант 1
# num = str(253523651)
# print(num)
# first = tuple(num)
# print(first)
# print(first.count(2))
#
#
# print("2 =", first.count(2))
# print("5 =", first.count(5))
# print("3 =", first.count(3))
# print("6 =", first.count(6))
# print("1 =", first.count(1))

# Вариант 2 ---------------------------------------------------------------

# tpl = tuple(input('Введите элементы кортежа: '))
# lst = []
# print(tpl)
# for num in tpl:
#     if num not in lst:
#         lst.append(num)
#         print(f'Количеств {num} = {tpl.count(num)}')


# 16.12.2023   --------------------------------------------------

# Множество  (set)

# s = {"banana", "apple", "orange", "banana", "apple"}
# print(s)
# print(type(s))
# print(len(s))

# c = ["red", "blue", "green", "red"]
#
# a = set(c)
# print(a, type(a))

# mas = [1, 2, 3, 2, 3, 4, 4, 5]
#
# s = {x for x in mas if x % 2 == 0}
# print(s)

# def to_set(element):
#     st = set(element)
#     return st, len(st)
#
# print(to_set("Я обычная строка"))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# t = {"red", "green", "blue"}
# # print("green" not in t)
#
# for i in t:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# a = [i for i in r if 'a' not in i]
# a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r]
# a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c']
# print(a)

# a = {"Tom", "Bob", "Alice"}
# print(a)
# a.add("Anna")
# print(a)
# a.remove("Anna") #  Ann1 при обращении к несуществующему элементу - ошибка  KeyError
# print(a)
# user = "Tom"
# if user in a:
#     a.remove(user)
# print(a)

# a.discard("Anna")
# print(a)

# a.pop()
# print(a)

# n = a.pop()
# print(n)
# print(a)
# a.clear()
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # a |= b
# # c = a & b
# # print(c)
# # a &= b
# # c = a ^ b
# # print(c)
# a ^= b
# print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# count = len(s)
# print("Count", count)
# print("Min", min(s))
# print("Max", max(s))
# print("Sum", sum(s))

# s1 = set("Hello")
# s2 = set("How are you")
# a = s1 & s2
# print(a)
# for i in a:
#     print(i, end=" ")

# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
#
# # a = drawing.union(music)
# # print(a)
# one_hobby = drawing ^ music
# print("Один кружок: ", one_hobby)
#
# both_hobby = drawing & music
# print("Оба кружка: ", both_hobby)
#
# # drawing = drawing - both_hobby
# drawing -= both_hobby
# print("Кружок рисования: ", drawing)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a <= b)
# print(a >= b)

# Тип frozenset  замороженный сет

# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# print(type(s))
# a = frozenset({"hello", "world"})
# print(a)

# a = [0, 1, 2, 3, 4, 5, 6, 8, 4, 7, 5, 1, 2, 5, 4, 88, 9]
# print(a)
# b = set(a)
# print(b)
# a = tuple(b)
# print(a)

# s = input("Введите строку: ")
# count = 0
# str_1 = set("уеэоаяюи")
# for str_2 in s:
#     if str_2 in str_1:
#         count += 1
# print("Количество гласных равно: ",(count))


# Словарь 'dict'--------------17.12.2023--------------------------------------------------------

# lst = [1, 2, 3]
# d = {'one': 1, 'two': 2, 'three': 3}
# lst[0] = 10
# print(lst[0])
# d['one'] = 10
# print(d['one'])

# d = {}
# print(d)
# print(type(d))

# d = {0: 1, 'one': 45,}

# d = {a: a ** 2 for a in range(7)}
# print(d)

# d = {'one': 1, 'two': 2, 'four': 4}
# key = "four1"
#
# # if key in d:
# #     del d[key]
#
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом " + key + " нет в словаре")
#
# # print('one1' in d)
# for i in d:
#     print(i, "->", d[i])

# Задача--------

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# com = 1
# for key in d:
#     com *= d[key]
# print('Произведение :', com)


# Задача-----------------------
# d = dict()  вывод варианта 1
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# d = {i: input("-> ") for i in range(1, 5)}  # вариант 2
#
# print(d)
# dislike = int(input("Введите элемент исключить "))
# del d[dislike]
# print(d)

# myDict = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(len(myDict))
# print(min(myDict))
# print(max(myDict))

#  Задача---------------------

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670', 3, 8500],
#     '3': ['AMD FX=6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400]
# }
# for i in goods:
#     print(i, ")", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input('№: ')
#     if n != '0':
#         if n in goods:
#             qty = int(input('Количество: '))
#             goods[n][1] += qty
#         else:
#             print('Некорректный номер товара! Х')
#     else:
#         break
# for i in goods:
#     print(i, ")", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб", sep="")
#

# d = {'a': 1, 'b': 2, 'c': 3}
#
# print(d.keys()) # список ключей
# print(d.values()) # список значений
# print(d.items()) # список ключей и значений
#
# # for i, j in d.items():
# #     print(i, "->", j)
#
# print(list(d.values()))

# d = {'a': 1, 'b': 2, 'c': 3}
#
# d2 = d.copy()
#
# print("d:", d, id(d))
# print("d2:", d2, id(d2))
#
# d2['a'] = 5
# d['e'] = 7
#
# print("d:", d, id(d))
# print("d2:", d2, id(d2))
#
# d.clear()
# print("d:", d, id(d))
# print("d2:", d2, id(d2))


# d = {'a': 1, 'b': 2, 'c': 3}

# print(d['e'])
# value = d.get('b', "Такого ключа не существует")
# print(value)

# item = d.popitem()
# print(item)
# print(d)

# d_dict = {'name': 'Kellu', 'age': 25, 'salary': 8000, 'city': 'New York'}
# print("Словарь: ", d_dict)
# d_dict.pop('age')
# d_dict.pop('city')
# print(d_dict)
# f = d_dict.update('age')
# i = ['age', 'city']
# for key in i:
#     del d_dict[key]
# print(str(d_dict))
#
# print("Новый словарь: ", d_dict)

# item = d_dict.popitem()
# item_1 = d_dict.pop('age')
# print(item,item_1)
# print(d_dict)

# Домашняя работа от 16.12.2023 или 17.12.2023--------------------------------------------------------
# VOWELS = {'а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я', 'ё'}
#
# string = input('Введите строку: ')
#
# # count = 0
# # for letter in string:
# #     if letter.lower() in VOWELS:
# #         count += 1
# #
# # print('Количество гласных равно:', count)
#
# tmp_list = [letter for letter in string if letter.lower() in VOWELS]
#
# print('Количество гласных равно:', len(tmp_list))


# 23.12.2023--------------------------------

# d = {'a': 1, 'b': 2, 'c': 3}
#
# d1 = {'r': 7, 'q': 40}
# d.update(d1)
# # d2 = {'a': 20, 'b': 9}
# d2 =[('a', 20), ('b', 9)]
# d.update(d2)
# print(d)


# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # new_disc = x.copy()
# # new_disc.update(y) или--
#
# new_disc = x | y
#
# print(new_disc)   работает


# a = {
#     'first':{
#         1:'one',
#         2:'two',
#         3:'three'
#     },
#     'second':{
#         4:'four',
#         5:'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t", y, ": ", a[x][y], sep="")  # работает


# sales = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#          "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#          "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#          "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ": ", sales[x][y], sep="")
#
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_date = int(input("Новое значение: "))
# sales[person][region] = new_date
# print(sales[person])  # работает  и можно добавить ниже обработку ошибок
#
# try:
#     person = input('Введите имя: ')
#     saler = sales[person]
#     try:
#         region = input('Введите регион: ')
#         new_data = int(input('Введите новое значение: '))
#         sales[person][region] = new_data
#         print(sales[person])
#     except (KeyError, ValueError):
#         print('Такого региона нет')
# except KeyError:
#     print('Такого продавца нет.')


# d = {"N": 3056, "S": 8463, "E": 8441, "W": 2694}
# new_d = {value: key for key, value in d.items()}
# print(new_d)


# d = {"N": 1, "S": 2, "E": 3, "W": 4}
# # new_d = {k: v for k, v in d.items() if v <= 2}
# # print(new_d)
#
# for i in range(2):
#     print('key:', list(d.items())[i][0], 'value:', list(d.items())[i][1])

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# c = list(d)
# for key in c[:2]:
#     print(f'{key}: {d[key]}')

# Перемена_____________---------------

# d = {"N": 1, "S": 2, "E": 3, "W": 4}
# value = list(d.items())
# print(value)
#
# value = list(d)
# print(value)


# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = {}
# current_key = ""
#
# for item in a:
#
#     if type(item) is str:
#         d[item] = []
#         current_key = item
#     else:
#         d[current_key].append(item)
#
# print(d)  # задача работает

# d = dict(zip([1,2,3], ['one','two','three']))
# print(d)
#
# a = [1,2,3]
# b = ['one','two','three']
# f = {k: v for k, v in zip(a, b)}
# print(f)

# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# # c = tuple(zip(a, b))
# # c = list(zip(a, b))
# # c = set(zip(a, b))
# c = dict(zip(a, b))
# print(c)


# d_one = {'name':"Igor", "Last_name": "Petrov", "job": "Consultant"}
# d_two = {'name': "Irina", "Last_name": "Irisova", "job": "Manager"}
# for (k1, v1), (k2, v2) in zip(d_one.items(), d_two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)  # работает


# d = ([(1, 'one'), (2, 'two'), (3, 'three')])
# a, b = zip(*d)
# print(a)
# print(b)


# a = ('one', 'two', 'three')
# b = [1, 2, 3,]
# d = dict(zip(a, b))
# print(d)
# s = sorted(d.items())
# print(s)
# print(dict(s))


# one = {'apple': 0.45, 'orange': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
# print({**one, **two})  #{'apple': 0.45, 'orange': 0.35, 'pepper': 0.2, 'onion': 0.55}
# for k, v in {**two, **one}.items():
#     print(k, "->", v)


# data = ["red", "green", "blue"]
# num = 0
# for val in data:
#     print(num, ") ", val, sep="")
#     num += 1
# print()
# for num, val in enumerate(data, start=10):
#     print(num, ") ", val, sep="")

# Домашняя работа

# month = ["January", "February", "Match"]
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
# for sales, costs, m in zip(total_sales, prod_cost, month):
#     profit = sales - costs
#     print("Чистая прибыль в :", m, "=", profit)


# 24.12.2023 -----------------------------------------------------

# a = [1, 2, 3]
# b = [a, 4, 5, 6]
# print(b)
# c = [*a, 4, 5, 6]
# print(c)

# def func(*args):
#     # print(args)
#     return args
#
#
# print(func(2))
# print(func(2, 3, 4, "abc"))
# print(func())

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(3, 4, 5))

# Задача-----
# def to_dict(*args):
#     return {element: element for element in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict("grey", (2, 17), 3.11, -4))  # работает\

# Задача
# def func(*args):
#     midle = sum(args)/len(args)
#     print(midle)
#     res = []
#     for element in args:
#         if element < midle:
#             res.append(element)
#     return res
# first = func(1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(first)
# second = func(3, 6, 1, 9, 5)
# print(second) # работает

# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, 4, 5, 6, 7, ))


# def print_score(student, *scores):
#     print("Student Name:", student)
#     for score in scores:
#         print(score)
# print_score("Irina", 5,4,3,2,5)
# print_score("Igor", 5,4,5,3,2,5)
# print_score("Lev")

# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {"one": "first"}
# db(k1=11, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, wight=61, eyes_color='grey')
# print(my_dict)

# def func(a,*args, **kwargs):
#     return a, args, kwargs
#
#
# print(func(5,9,7,8,4,3,2,1, k1=11, k2=31, k3=11, k4=91,d=55))


# name = "Tom"
# # print("Глобальная область видимости: ", id(name))
#
# def hi():
#     global name
#     name = "Sam"
#     # print("Локальная область видимости:", id(name))
#     surname = "Johnson"
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# hi()
# bye()
# print(name)


# i = 5
# def func(arg=i):
#     print(arg)
#     arg += 1
#     return arg
# print(func(arg=10))
# print(func(i))
#
# i = 6
# func()


# def add_five(a):
#     x = 2
#
#     def add_some():
#         print("x =", x)
#         return a + x
#     return add_some()
#
# print(add_five(5))


# sum = 5
#
# lst = [9, 5, 8, 7, 6]
# print(sum(lst))


# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)
#     print(type(t))
#     print(dir(t))


# n = int(input("Введите количество студентов: "))
#
# students = {}
#
#
# for name in range(1, 5):
#
#     name, module, ball = input().replace(' (', '#').replace('): ', '#').split('#')
#     ball = int(ball)
#     if name in students:
#         students[name][module] = students[name].get(module, 0) + ball
#     else:
#         students[name] = {module: ball}
#
# for key in students:
#     if len(students[key]) == 5 and sum(students[key].values()) >= 75:
#         print(key)

#


# 30.12.2023-------------------

# def outer(who):
#      a = 5
#      def inner():
#          print("Hello", who)
#
#      inner()
#
# outer()


# def fun1():
#     a=6
#
#     def fun2(b):
#         a=4
#         print(a + b)
#
#     print("a", a)
#     fun2(4)
#
#
# fun1()


# x = 25
# t = 0
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("a", a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t
# print(c)


# def fn1():
#     x = 25 # 2
#
#     def fn2():
#         x = 33 # 4
#
#         def fn3():
#             nonlocal x
#             x = 55 # 6
#
#             # print("fn3.x =", x) # 9
#         fn3() # 5
#         print("fn2.x =", x) # 7
#
#     fn2() # 3
#     print("fn1.x =", x) # 8
#
# fn1() # 1


# def outer(a1,b1,a2,d2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + d2
#
#     inner()
#     return [a,b]
#
# res = outer(2,3,-1,4)
# print(res) # [список [1, 7 ]]


# Замыкание --------------------------------

# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# item1 = outer(5)
# print(item1(10))
#
# item2 = outer(5)
# print(item2(1))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1,2,3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a += 1
#         b += "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     s = 0
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#     return inner
# res1 = func('Moscow')
# res1()
# res1()
# res2 = func('sochi')
# res2()
# res2()
# res2()
# res1()
# res3 = func('Kyev')
# res3()
# res3()
# res3()

# lambda(анонимная функция)


# print((lambda x, y: x + y)(1, 2))
#
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func('a', 'b'))


# print((lambda x, y: x ** 2 + y ** 2)(2, 5))
# print((lambda x, y = 5: x ** 2 + y ** 2)(2, ))
# print((lambda x = 2, y = 5: x ** 2 + y ** 2)())
# print((lambda x = 2, y = 5: x ** 2 + y ** 2)(10, 20))
# print((lambda x = 2, y = 5: x ** 2 + y ** 2)(y = 10))


# print((lambda *args: args)(1, 2, 3, 4, 5))


# y = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
# for i in y:
#     print(i("abc__"))
#


# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# f = outer(5)
# print(f(10))
#
#
# def outer1(n):
#     return lambda x: x + n
#
#
# f1 = outer1(5)
# print(f1(10))
#
# outer2 = lambda n: lambda x: x + n
#
# f2 = outer2(5)
# print(f2(10))
#
# print((lambda n: lambda x: x + n)(5)(10))


# print((lambda x: lambda y: lambda z: x + y + z) (2)(4)( 6))


# def func(item):
#     return item[1]


# d = {'b':3, 'c': 1, 'a': 2}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# # lst.sort(key=func)
# print(lst)
# d1 = dict(lst)
# print(d1)


# player = [
#     {'name':'Anton', 'last name': 'Bipykov', 'rating': 9},
#     {'name':'Aleksey', 'last name': 'Bodny', 'rating': 10},
#     {'name':'Fedor', 'last name': 'Sidorov', 'rating': 4},
#     {'name':'Mihail', 'last name': 'Semenov', 'rating': 6},
# ]
# res = sorted(player, key=lambda i: i['last name'])
# print(res)
# res = sorted(player, key=lambda i: i['rating'], reverse=True)
# print(res)


# a =[
#     lambda x, y: x + y,
#     lambda x, y: x - y,
#     lambda x, y: x * y,
#     lambda x, y: x / y,
#     lambda x, y: x // y,
#     lambda x, y: x % y,
# ]
#
# print(a[0](5, 2))
# print(a[1](5, 2))
# print(a[2](5, 2))
# print(a[3](5, 2))
# print(a[4](5, 2))
# print(a[5](5, 2))


# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье"),
# }
#
# d[6]()


# print((lambda a, b: a if a > b else b)(15, 23))


# print((lambda a, b, c: a if (a < b and a < c) else (b if b < c else c))(18, 19, 17))


# Домашняя работа от 30.12.2023---------------------------------------------------------------------------------------
# from math import pi
#
# lambda_x_y_z = [
#     lambda x: print(f'Площадь окружности радиуса {x}: {x ** 2 * pi}'),
#     lambda x, y: print(f'Площадь прямоугольника размером {x}*{y}: {x * y}'),
#     lambda a, b, h: print(f'Площадь трапеции a={a}, b={b}, h={h}: {(a + b) * h/2}'),
# ]
#
# lambda_x_y_z[0](2)
# lambda_x_y_z[1](10, 13)
# lambda_x_y_z[2](7, 5, 3)

# ---------------------------------------------------------------------------------------------------------------------


# f = open(r'C:\Users\User\PycharmProjects\pythonProject1\test.txt, mode= 'r')
# f = open('test.txt', 'r')
# print(*f)
# print(f)
# f.close()
# print(f.close)
# print(f.mode)
# print(f.name)
# print(f.encoding)


# f = open('test.txt', 'r')
# print(f.read(3))
# print(f.read())
# f.close()

# f = open('test1.txt', 'r')
# #print(f.read())
# print(f.readline())
# print(f.readline(9))
# print(f.readline())
# f.close()


# f = open('test1.txt', 'r')
# print(f.readlines(16))
# print(f.readlines())
# f.close()

# f = open('test1.txt', 'r')
# count = 0
# for line in f:
#     print(line)
#     count += 1
# f.close()
# print("count =", count)  # подсчитывает количество строк в файле = 3


# f = open("xyz.txt", "w")
# f.write("Hello\nWorld\n")
#
# f.close()


# f = open("xyz.txt", "a")
# f.write("New text.\nOpen text in Explorer")
# f.close()
#
#
# f = open("test.txt", "a")
# f.write("This is a factor")
# f.close()


# f = open("xyz.txt", "w")
# line = ['This is line 1\n', 'This is line 2']
# f.writelines(line)
# f.close()

# --------------------------------------------------------------------------------------------------------------
# Домашняя работа от 27.01.2024-===============================================================================
# import re

# data = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78'
#
# pattern = r'\+*\d{1}\s*\(*\s*\d{3}\s*\)*\s*\d{3}[\s-]*\d{2}[\s-]*\d{2}'
#
# print(re.findall(pattern, data))

# ==============================================================================================================

# 28.01.2024

# data = [0, -2, 3, 9, -11, -4, -5, 6, 7, 7, -1]
#
# def count_negative(lst: list) -> int:
#     count = 0
#     if not lst:
#         return count
#     for i in range(1, len(lst) + 1):
#         if lst[i - 1] < 0:
#             count += 1
#         else:
#             return count + count_negative(lst[i:])
#     return count
#
# print(count_negative(data))

# ==============================================================================================================

#


# class Stack:
#     def __init__(self):
#         print("Hi!")
#
# stackObject = Stack()


# class Stack:
#     def __init__(self):
#         self.__stacklist = [] # инкапсуляция - нельзя переменную увидеть из вне
# stackObject = Stack()
# print(len(stackObject.stacklist)) # выход - AttributeError


# class Stack:
#     def __init__(self):
#         self.__stacklist = []
#
#     def push(self, value):
#         self.__stacklist.append(value)
#
#     def pop(self):
#         value = self.__stacklist[-1]
#         del self.__stacklist[-1]
#         return value
#
#
# stackObject = Stack()
#
# stackList.push(3)
# stackList.push(2)
# stackList.push(1)
#
# print(stackList.pop())
# print(stackList.pop())
# print(stackList.pop())


# class Stack:
#     def __init__(self):
#         self.__stacklist = []
#
#     def push(self, val):
#         self.__stacklist.append(val)
#
#     def pop(self):
#         value = self.__stacklist[-1]
#
#     del self.__stacklist[-1]
#     return val
#
#
# stackObject1 = Stack()
# stackObject2 = Stack()
#
# stackObject1.push(3)
# stackObject2.push(stackObject1.pop())
# print(staclObject2.pop())


# for i in range(5):
#     nam = int(input())
#     nam1 = int(input())
#
#     print("Разность: ", nam - nam1)
#
# print("Вызов завершён")


# a = int(input("Введите числитель: "))  #-------------------------------- Программа при делении на 0 делить нельзя.
# b = int(input("Введите знаменатель: "))
# print('Результат : ', a/b if b else 'На ноль делить нельзя!!!')


# try:
# 	n = int(input("введите делимое : "))  #---------------------------------- программа с использованием исключений
# 	m = int(input("введите делитель : "))
# 	print("результат : ", n / m)
# except (ValueError, ZeroDivisionError):
# 	print("На ноль или строки вводить или делить нельзя")
# else:
# 	print("Всё нормально вы ввели : ", n, "и", m)
# finally:
# 	print("конец программы")


# n = input("введите число : ") # программа складывае равные по типу данных или конкатенация строк, строк+числа
# m = input("введите число : ")
#
# try:
#     n = int(n)
#     m = int(m)
# # print(int(n) + int(m))
# except ValueError:
#     n = str(n)
# # print(str(n) + str(m))
# finally:
#     print("программа завершилась", n + m)
#
#
# i = 1 # программа выводит только чётные числа в диапазоне от 1 до 20
# while i <= 20:
#     if i % 2 == 0:
#         print("i = ", i)
#     i += 1


# 25.11.2023 -------------------------------

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
#     else:
#         print('done')

# for i in range(1):
#     print("+++ i  =", i)
#     for j in range(2):
#         print("----- j =", j)

# w = int(input("Введите ширину прямоугольника: "))  # программа вывода прямоугольника
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# nums = [letter * 2 for letter in "Banana"]

# nums = [i for i in range(30) if i % 2 == 0] # Выводит чётные числа
# print(nums)

# Список

# nums = [8, 3, 9, 4, 1, "one"]
# print(nums)
# print(type(nums))
# print(nums[-2])
# # print(nums[0])
#
# nums[1] = 256
# print(nums)
# nums[3] += 100
# print(len(nums))
# for i in range(len(nums)):
#     print(nums[i] + 2)

# for i in range(1, 10):  # Таблица умножения
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     print("\n")

# s = []
# print(s)
#
# b = list()
# print(b)  #  досмотреть и дописать 11:10 время

# a = [0 for _ in range(5)]  # нижнее подчёркивание это зарезервированное имя
# print(a)
# b = [_ for _ in range(5)]
# print(b)

# n = 5
# b = [i ** 2 for i in range(1, n + 1)]
# print(b)

# a, b = [1, 2, 3], [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = input("-> ")
# print(a)

# a = [input(">->-> ") for i in range(int(input("n = ")))]
# print(a)
#
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end="")

#  26.11.2023 ---------------

# a = [1, 2, 3, 4, 5, 6, 7]
# # print(a)
# # # a[0], a[1] = a[1], a[0]
# # print(a)
# # print(a[3:])
# # print(a[::2])
# a[1:3] = [0, 0, 0, 0]
# print(a)

# s = [5, 9, 3, 7, 1, 8]
# s.append(99)
# print(s)
# s.extend([1, 2, 3])
# print(s)
# s.insert(3, 100)
# print(s)
# s.extend('add')
# print(s)

# s = []
# n = int(input("Кол-во эл. списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.insert(0, x)
# print(s)

# задача выводит числа кратные 3
# s = []
# n = int(input("Кол-во элементов: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print("Число не кратно 3: ")
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
#
# print(c)

# a = [1, 2, 3]   #  сложить два списка и записать результат в с значение индексов 1+1; 2+2 ...
# b = [11, 22, 33]
# c = []
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)

# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33]
# c = []
#
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])

# if len(b) > len(a):
#
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

#
# s = [5, 9, 3, 7, 1, 8, 9, 9]
# print(s)
# s.remove(9)
# print(s)

# n = ......  #  дописать 12:40 - 12:50

# s = [5, 9, 3, 7, 9, 1, 8, 9]
# print(s)
# num = s.count(9)
# # print(num)
#
# ind = s.index(9) #  возвращает индекс первого искомого элемента
# print(ind)
# ind = s.index(9, 5)
# print(ind)

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# b = []
# for i in a:
#     if i != a[0. i]:
#         b.append(i)
#         break
# print(b)


#  02.12.2023____------------------
# a = [1, 2, 3]
# b = a.copy()
# print("a =",a)
# print("b =",b)
#
# a.append(20)
# print("a =",a)
# print("b =",b)
# b.append(120)


# a = [5, 4, 1, 2, 3]
# print(a)
# # a.reverse()
# # print(a)
#
# # a.sort()
# # print(a)
# a.sort(reverse=True)
# print(a)


# b =["Виталий","Сергей","Александр","Анна"]
# b.sort(key=len, reverse=True)
# print(b)

# a = [5, 4, 1, 2, 3]
# print(a)
# a.sort()
# print(a)

# sort = sorted(a)
# print(sort)

#  Генерация случайных данных  ----->----------->-------------->------------->------------->


# print(random.random())
# print(random.randint(3, 9))
# print(random.randrange(3, 9))
#
# print(round(random.uniform(10.5, 25.5), 2))

# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(random.choice(city_list))
# print(random.choices(city_list, k=3))
# random.shuffle(city_list)
# print(city_list)


# s = [55, 66, 77, 88, 99, 9, 8, 7, 6, 5, 4, 1, 2, 3]
# print(random.choice(s))
# print(random.choices(s, k=5))

# lst = [5, 4, 3, 2, 1]
# print(len(lst))
# print(sum(lst))
# print(min(lst))
# print(max(lst))

# Задача --------------------------------

# import random
# mas = [random.randint(0, 20) for i in range(10)]
# print(mas)

# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# mas_ = max(mas)
# print(mas_)
# mas.remove(mas_)
# mas.insert(0, mas_)
# print(mas)  #  вариант 1 программа работает

# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# max_ = max(mas)
# print(max_)
# mas.remove(max_)
# mas.insert(0, max_)
# print(mas)    # вариант 2 программа работает

#  Перемена--------------------------------
# Задача : программа находит мин значение и выводит в новый список с удалением других объектов впереди себя
# import random
#
# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
#
# min_ch = min(lst)
# print("min =", min_ch)
#
# ind_min = lst.index(min_ch)
# print("index min =", ind_min)
#
# del lst[: ind_min]
# print(lst)
# print(lst(ind_min))  # перепроверить

# lst = [5]
# print(lst)
# if not lst:
#     print("Список пуст")
# else:
#     print("В списке есть элементы")

# import random
#
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
#
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print("Третий список: ", c)
# d = []
# for element in a:
#     if element not in d:
#         d.append(element)
# for element in b:
#     if element not in d:
#         d.append(element)
# print("Элементы обоих списков без повторений: ", d)
# c = []
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print("Элементы общие для обоих списков: ", c)

# c = [min(a), min(b), max(a), max(b)]
# print(c)    # задача работает

#  ----- Домашняя работа от 02,12,2023


# import random
#
# print(random.sample(range(1, 10+1), 10))

# a = [random.randint(0, 10) for i in range(10)]
# b = []
# for element in a:
#     if element not in b:
#         b.append(element)
# print(b)

# import random
#   a = [random.randint(1, 10) for i in range(10)]
# for v in range(1, 10):
#     v = 2 ** v
#     b = list(random_range(v))
#     print("Need", v, "found", len(set(b)), "(min,max)", (min(b), max(b)))
# print("", b)
# print()

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# # m = ["Hello", "World"]
# print(m)
# # print(len(m))
# # print(m[1][2])
# print()
# # for row in range(len(m)):
# #     for col in range(len[row]):
# #         print(m[row][col], end="\t")
# #         print()
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()


# 10.02.2024--------------------------------------------------------
#  в классе могут быть свойства (поля, переменные)
#  методы(функции). Имя класса пишется в верхнем регистре
#  пропускаем 2 пустых линии.
# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 24
# # print(p1.x)
# # print(p1.y)
# # print(p1.__dict__)
# # print(id(p1))
# p1.set_coord(5, 24)
# Point.set_coord(p1, 5, 24)
#
#
# p2 = Point()
# # p2.x = 10
# # print(p2.x)
# # print(p2.y)
# # print(p2.__dict__)
# # print(id(p2))
# #
# # print(id(Point))
# p2.set_coord(10, 30)
#
# # 10:36-- дописать
# # 10.57 -- продолжим --------------------------------

#  задача ---------------------------------------------

# class Human():
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n"
#               f"Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_address(self, address):  # Устанавливает замену адрессса
#         self.address = address
#
#     def get_address(self):  # получаем адресс
#         return self.address
#
#     def __set_name__(self, name):  # Устанавливаем имя
#         self.name = name
#
#     def get_name(self):  # Получаем имя
#         return self.name
#
#
# h1 = Human()
# # h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1A")
#
# h1.print_info()
# # h1.set_address("ул.Ленина, 56")
# # print(h1.get_address())
# # h1.__set_name__("Юлия")
# # print(h1.get_name())


# ----------------------------------------------------------------
# Задача

# class Person:
#     skill = 10  # Статическое свойство(имеют первоначальные значения)
#     count = 0  # считает количество экземпляров класса
#
#     # name = ""
#     # surname = ""
#
#     def __init__(self, name, surname):
#         self.name = name  # Динамические свойства
#         self.surname = surname
#         #print("Иннициализатор класса", self)
#         # self.count += 1 # обращаться к статическим свойствам через экземпляр класса
#         Person.count += 1 # обращаться к статическим свойствам через Имя класса
#
#     # def __del__(self):
#     #     print("Удаления экземпляра: ", self)
#     #
#     # def print_info(self):
#     #     print("Данные сотрудники: ", self.name, self.surname)
#     #
#     # def add_skill(self, k):
#     #     self.skill += k
#     #     print("Квалификация сотрудника: ", self.skill, end="\n\n")
#
#
# p1 = Person("Виктор", " Резник")
# # p1.print_info()
# # p1.add_skill(3)
# # del p1
# # p1 = 5
# print(p1.count)
#
# p2 = Person("Анна", "Долгих")
# # p2.print_info()
# # p2.add_skill(2)
# print(p2.count)
# print(Person.count)

# ------------------------------------------------------------------------------------------------
# Задача

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота: ", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается")
#
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print(self.name, "был последним")
#
#     def sey_hi(self):
#         print("Приветствую! Меня зовут: ", self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.sey_hi()
# print("Численность роботов: ", Robot.k)
#
# droid2 = Robot('C-3PO')
# droid2.sey_hi()
# print("Численность роботов: ", Robot.k)
#
# droid3 = Robot('S-9PO')
# droid3.sey_hi()
# print("Численность роботов: ", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу\n")
#
# print("Роботы закончили свою работу. Давайте их выключим.")
# del droid1
# del droid2
# del droid3
#
# print("Численность роботов: ", Robot.k)


# 11.02.2024 -------------------------------------------------------------------------------------------------


# def set_param(c=20, s="-"):
#     print(s * c)
#
#
# set_param()
# set_param(7)
# set_param(5, "*")

# 16.12.2023   --------------------------------------------------

# Множество  (set)

# s = {"banana", "apple", "orange", "banana", "apple"}
# print(s)
# print(type(s))
# print(len(s))

# c = ["red", "blue", "green", "red"]
#
# a = set(c)
# print(a, type(a))

# mas = [1, 2, 3, 2, 3, 4, 4, 5]
#
# s = {x for x in mas if x % 2 == 0}
# print(s)

# def to_set(element):
#     st = set(element)
#     return st, len(st)
#
# print(to_set("Я обычная строка"))
# print(to_set([4, 5, 4, 6, 2, 9, 11, 3, 4, 2]))

# t = {"red", "green", "blue"}
# # print("green" not in t)
#
# for i in t:
#     print(i)

# r = ['ab_1', 'ac_2', 'bc_1', 'bc_2']
# # a = [i for i in r if 'a' not in i]
# # a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r]
# a = ['A' + i[1:] if i[0] == 'a' else 'B' + i[1:] for i in r if i[1] == 'c']
# print(a)

# a = {"Tom", "Bob", "Alice"}
# print(a)
# a.add("Anna")
# print(a)
# a.remove("Anna") #  Ann1 при обращении к несуществующему элементу - ошибка  KeyError
# print(a)
# user = "Tom"
# if user in a:
#     a.remove(user)
# print(a)

# a.discard("Anna")
# print(a)

# a.pop()
# print(a)

# n = a.pop()
# print(n)
# print(a)
# a.clear()
# print(a)

# a = {0, 1, 2, 3}
# b = {4, 3, 2, 1}
# # c = a.union(b)
# # c = a | b
# # a |= b
# # c = a & b
# # print(c)
# # a &= b
# # c = a ^ b
# # print(c)
# a ^= b
# print(a)

# s1 = {1, 2}
# s2 = {3}
# s3 = {4, 5}
# s4 = {3, 2, 6}
# s5 = {6}
# s6 = {7, 8}
# s7 = {9, 8}
#
# # s = s1.union(s2, s3, s4, s5, s6, s7)
# s = s1 | s2 | s3 | s4 | s5 | s6 | s7
# print(s)
# count = len(s)
# print("Count", count)
# print("Min", min(s))
# print("Max", max(s))
# print("Sum", sum(s))

# s1 = set("Hello")
# s2 = set("How are you")
# a = s1 & s2
# print(a)
# for i in a:
#     print(i, end=" ")

# drawing = {'Марина', 'Женя', 'Света'}
# music = {'Костя', 'Женя', 'Илья'}
#
# # a = drawing.union(music)
# # print(a)
# one_hobby = drawing ^ music
# print("Один кружок: ", one_hobby)
#
# both_hobby = drawing & music
# print("Оба кружка: ", both_hobby)
#
# # drawing = drawing - both_hobby
# drawing -= both_hobby
# print("Кружок рисования: ", drawing)

# a = {0, 1, 2, 3, 4}
# b = {3, 2, 1}
# print(a <= b)
# print(a >= b)

# Тип frozenset  замороженный сет

# s = frozenset([1, 2, 3, 4, 5])
# print(s)
# print(type(s))
# a = frozenset({"hello", "world"})
# print(a)

# a = [0, 1, 2, 3, 4, 5, 6, 8, 4, 7, 5, 1, 2, 5, 4, 88, 9]
# print(a)
# b = set(a)
# print(b)
# a = tuple(b)
# print(a)

# s = input("Введите строку: ")
# count = 0
# str_1 = set("уеэоаяюи")
# for str_2 in s:
#     if str_2 in str_1:
#         count += 1
# print("Количество гласных равно: ",(count))


# Словарь 'dict'--------------17.12.2023

# lst = [1, 2, 3]
# d = {'one': 1, 'two': 2, 'three': 3}
# lst[0] = 10
# print(lst[0])
# d['one'] = 10
# print(d['one'])

# d = {}
# print(d)
# print(type(d))

# d = {0: 1, 'one': 45,}

# d = {a: a ** 2 for a in range(7)}
# print(d)

# d = {'one': 1, 'two': 2, 'four': 4}
# key = "four1"
#
# # if key in d:
# #     del d[key]
#
# try:
#     del d[key]
# except KeyError:
#     print("Элемента с ключом " + key + " нет в словаре")
#
# # print('one1' in d)
# for i in d:
#     print(i, "->", d[i])

# Задача--------

# d = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# com = 1
# for key in d:
#     com *= d[key]
# print('Произведение :', com)


# Задача-----------------------
# d = dict()  вывод варианта 1
# d[1] = input("-> ")
# d[2] = input("-> ")
# d[3] = input("-> ")
# d[4] = input("-> ")
# d = {i: input("-> ") for i in range(1, 5)}  # вариант 2
#
# print(d)
# dislike = int(input("Введите элемент исключить "))
# del d[dislike]
# print(d)

# myDict = {'x1': 3, 'x2': 7, 'x3': 5, 'x4': -1}
# print(len(myDict))
# print(min(myDict))
# print(max(myDict))

#  Задача---------------------

# goods = {
#     '1': ['Core-i3-4330', 9, 4500],
#     '2': ['Core-i5-4670', 3, 8500],
#     '3': ['AMD FX=6300', 6, 3700],
#     '4': ['Pentium G3220', 8, 2100],
#     '5': ['Core-i5-3450', 5, 6400]
# }
# for i in goods:
#     print(i, ")", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб", sep="")
#
# while True:
#     n = input('№: ')
#     if n != '0':
#         if n in goods:
#             qty = int(input('Количество: '))
#             goods[n][1] += qty
#         else:
#             print('Некорректный номер товара! Х')
#     else:
#         break
# for i in goods:
#     print(i, ")", goods[i][0], " - ", goods[i][1], "шт. по ", goods[i][2], "руб", sep="")
#

# d = {'a': 1, 'b': 2, 'c': 3}
#
# print(d.keys()) # список ключей
# print(d.values()) # список значений
# print(d.items()) # список ключей и значений
#
# # for i, j in d.items():
# #     print(i, "->", j)
#
# print(list(d.values()))

# d = {'a': 1, 'b': 2, 'c': 3}
#
# d2 = d.copy()
#
# print("d:", d, id(d))
# print("d2:", d2, id(d2))
#
# d2['a'] = 5
# d['e'] = 7
#
# print("d:", d, id(d))
# print("d2:", d2, id(d2))
#
# d.clear()
# print("d:", d, id(d))
# print("d2:", d2, id(d2))


# d = {'a': 1, 'b': 2, 'c': 3}

# print(d['e'])
# value = d.get('b', "Такого ключа не существует")
# print(value)

# item = d.popitem()
# print(item)
# print(d)

# d_dict = {'name': 'Kellu', 'age': 25, 'salary': 8000, 'city': 'New York'}
# print("Словарь: ", d_dict)
# d_dict.pop('age')
# d_dict.pop('city')
# print(d_dict)
# f = d_dict.update('age')
# i = ['age', 'city']
# for key in i:
#     del d_dict[key]
# print(str(d_dict))
#
# print("Новый словарь: ", d_dict)

# item = d_dict.popitem()
# item_1 = d_dict.pop('age')
# print(item,item_1)
# print(d_dict)


# 23.12.2023--------------------------------

# d = {'a': 1, 'b': 2, 'c': 3}
#
# d1 = {'r': 7, 'q': 40}
# d.update(d1)
# # d2 = {'a': 20, 'b': 9}
# d2 =[('a', 20), ('b', 9)]
# d.update(d2)
# print(d)


# x = {'a': 1, 'b': 2}
# y = {'b': 3, 'c': 4}
# # new_disc = x.copy()
# # new_disc.update(y) или--
#
# new_disc = x | y
#
# print(new_disc)   работает


# a = {
#     'first':{
#         1:'one',
#         2:'two',
#         3:'three'
#     },
#     'second':{
#         4:'four',
#         5:'five'
#     }
# }
# print(a)
# for x in a:
#     print(x)
#     for y in a[x]:
#         print("\t", y, ": ", a[x][y], sep="")  # работает


# sales = {"John": {"N": 3056, "S": 8463, "E": 8441, "W": 2694},
#          "Tom": {"N": 4832, "S": 6786, "E": 4737, "W": 3612},
#          "Anne": {"N": 5239, "S": 4802, "E": 5820, "W": 1859},
#          "Fiona": {"N": 3904, "S": 3645, "E": 8821, "W": 2451}}
#
# for x in sales:
#     print(x)
#     for y in sales[x]:
#         print("\t", y, ": ", sales[x][y], sep="")
#
# person = input("Имя: ")
# region = input("Регион: ")
# print(sales[person][region])
# new_date = int(input("Новое значение: "))
# sales[person][region] = new_date
# print(sales[person])  # работает  и можно добавить ниже обработку ошибок
#
# try:
#     person = input('Введите имя: ')
#     saler = sales[person]
#     try:
#         region = input('Введите регион: ')
#         new_data = int(input('Введите новое значение: '))
#         sales[person][region] = new_data
#         print(sales[person])
#     except (KeyError, ValueError):
#         print('Такого региона нет')
# except KeyError:
#     print('Такого продавца нет.')


# d = {"N": 3056, "S": 8463, "E": 8441, "W": 2694}
# new_d = {value: key for key, value in d.items()}
# print(new_d)


# d = {"N": 1, "S": 2, "E": 3, "W": 4}
# # new_d = {k: v for k, v in d.items() if v <= 2}
# # print(new_d)
#
# for i in range(2):
#     print('key:', list(d.items())[i][0], 'value:', list(d.items())[i][1])

# d = {'один': 1, 'два': 2, 'три': 3, 'четыре': 4}
# c = list(d)
# for key in c[:2]:
#     print(f'{key}: {d[key]}')

# Перемена_____________---------------

# d = {"N": 1, "S": 2, "E": 3, "W": 4}
# value = list(d.items())
# print(value)
#
# value = list(d)
# print(value)


# a = ["one", 1, 2, 3, "two", 10, 20, "three", 15, 36, 60, "four", -20]
#
# d = {}
# current_key = ""
#
# for item in a:
#
#     if type(item) is str:
#         d[item] = []
#         current_key = item
#     else:
#         d[current_key].append(item)
#
# print(d)  # задача работает

# d = dict(zip([1,2,3], ['one','two','three']))
# print(d)
#
# a = [1,2,3]
# b = ['one','two','three']
# f = {k: v for k, v in zip(a, b)}
# print(f)

# a = [1, 2, 3]
# b = ['one', 'two', 'three']
# # c = tuple(zip(a, b))
# # c = list(zip(a, b))
# # c = set(zip(a, b))
# c = dict(zip(a, b))
# print(c)


# d_one = {'name':"Igor", "Last_name": "Petrov", "job": "Consultant"}
# d_two = {'name': "Irina", "Last_name": "Irisova", "job": "Manager"}
# for (k1, v1), (k2, v2) in zip(d_one.items(), d_two.items()):
#     print(k1, "->", v1)
#     print(k2, "->", v2)  # работает


# d = ([(1, 'one'), (2, 'two'), (3, 'three')])
# a, b = zip(*d)
# print(a)
# print(b)


# a = ('one', 'two', 'three')
# b = [1, 2, 3,]
# d = dict(zip(a, b))
# print(d)
# s = sorted(d.items())
# print(s)
# print(dict(s))


# one = {'apple': 0.45, 'orange': 0.35}
# two = {'pepper': 0.2, 'onion': 0.55}
# print({**one, **two})  #{'apple': 0.45, 'orange': 0.35, 'pepper': 0.2, 'onion': 0.55}
# for k, v in {**two, **one}.items():
#     print(k, "->", v)


# data = ["red", "green", "blue"]
# num = 0
# for val in data:
#     print(num, ") ", val, sep="")
#     num += 1
# print()
# for num, val in enumerate(data, start=10):
#     print(num, ") ", val, sep="")

# Домашняя работа

# month = ["January", "February", "Match"]
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200.00]
# for sales, costs, m in zip(total_sales, prod_cost, month):
#     profit = sales - costs
#     print("Чистая прибыль в :", m, "=", profit)


# 24.12.2023 -----------------------------------------------------

# a = [1, 2, 3]
# b = [a, 4, 5, 6]
# print(b)
# c = [*a, 4, 5, 6]
# print(c)

# def func(*args):
#     # print(args)
#     return args
#
#
# print(func(2))
# print(func(2, 3, 4, "abc"))
# print(func())

# def summa(*params):
#     res = 0
#     for i in params:
#         res += i
#     return res
#
#
# print(summa(1, 2, 3, 4, 5, 6, 7, 8, 9))
# print(summa(3, 4, 5))

# Задача-----
# def to_dict(*args):
#     return {element: element for element in args}
#
#
# print(to_dict(1, 2, 3, 4))
# print(to_dict("grey", (2, 17), 3.11, -4))  # работает\

# Задача
# def func(*args):
#     midle = sum(args)/len(args)
#     print(midle)
#     res = []
#     for element in args:
#         if element < midle:
#             res.append(element)
#     return res
# first = func(1, 2, 3, 4, 5, 6, 7, 8, 9)
# print(first)
# second = func(3, 6, 1, 9, 5)
# print(second) # работает

# def func(a, *args):
#     return a, args
#
#
# print(func(1))
# print(func(1, 2, 3, 4, 5, 6, 7, ))


# def print_score(student, *scores):
#     print("Student Name:", student)
#     for score in scores:
#         print(score)
# print_score("Irina", 5,4,3,2,5)
# print_score("Igor", 5,4,5,3,2,5)
# print_score("Lev")

# def db(**kwargs):
#     my_dict.update(kwargs)
#
#
# my_dict = {"one": "first"}
# db(k1=11, k2=31, k3=11, k4=91)
# db(name='Bob', age=31, wight=61, eyes_color='grey')
# print(my_dict)

# def func(a,*args, **kwargs):
#     return a, args, kwargs
#
#
# print(func(5,9,7,8,4,3,2,1, k1=11, k2=31, k3=11, k4=91,d=55))


# name = "Tom"
# # print("Глобальная область видимости: ", id(name))
#
# def hi():
#     global name
#     name = "Sam"
#     # print("Локальная область видимости:", id(name))
#     surname = "Johnson"
#     print("Hello", name, surname)
#
#
# def bye():
#     print("Good bye", name)
#
#
# hi()
# bye()
# print(name)


# i = 5
# def func(arg=i):
#     print(arg)
#     arg += 1
#     return arg
# print(func(arg=10))
# print(func(i))
#
# i = 6
# func()


# def add_five(a):
#     x = 2
#
#     def add_some():
#         print("x =", x)
#         return a + x
#     return add_some()
#
# print(add_five(5))


# sum = 5
#
# lst = [9, 5, 8, 7, 6]
# print(sum(lst))


# import builtins
#
# name = dir(builtins)
#
# for t in name:
#     print(t)
#     print(type(t))
#     print(dir(t))


# n = int(input("Введите количество студентов: "))
#
# students = {}
#
#
# for name in range(1, 5):
#
#     name, module, ball = input().replace(' (', '#').replace('): ', '#').split('#')
#     ball = int(ball)
#     if name in students:
#         students[name][module] = students[name].get(module, 0) + ball
#     else:
#         students[name] = {module: ball}
#
# for key in students:
#     if len(students[key]) == 5 and sum(students[key].values()) >= 75:
#         print(key)

#
# from typing import Union

# 30.12.2023---------------------------------------------------------------------

# def outer(who):
#      a = 5
#      def inner():
#          print("Hello", who)
#
#      inner()
#
# outer()


# def fun1():
#     a=6
#
#     def fun2(b):
#         a=4
#         print(a + b)
#
#     print("a", a)
#     fun2(4)
#
#
# fun1()


# x = 25
# t = 0
#
# def fn():
#     global t
#     a = 30
#
#     def inner():
#         nonlocal a
#         a = 35
#         print("a", a)
#
#     inner()
#     t = a
#
#
# fn()
# c = x + t
# print(c)


# def fn1():
#     x = 25 # 2
#
#     def fn2():
#         x = 33 # 4
#
#         def fn3():
#             nonlocal x
#             x = 55 # 6
#
#             # print("fn3.x =", x) # 9
#         fn3() # 5
#         print("fn2.x =", x) # 7
#
#     fn2() # 3
#     print("fn1.x =", x) # 8
#
# fn1() # 1


# def outer(a1,b1,a2,d2):
#     a = 0
#     b = 0
#
#     def inner():
#         nonlocal a, b
#         a = a1 + a2
#         b = b1 + d2
#
#     inner()
#     return [a,b]
#
# res = outer(2,3,-1,4)
# print(res) # [список [1, 7 ]]


# Замыкание --------------------------------

# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# item1 = outer(5)
# print(item1(10))
#
# item2 = outer(5)
# print(item2(1))


# def func1():
#     a = 1
#     b = 'line'
#     c = [1,2,3]
#
#     def func2():
#         nonlocal a, b
#         c.append(4)
#         a += 1
#         b += "_new"
#         return a, b, c
#
#     return func2
#
#
# func = func1()
# print(func())


# def func(city):
#     s = 0
#     def inner():
#         nonlocal s
#         s += 1
#         print(city, s)
#     return inner
# res1 = func('Moscow')
# res1()
# res1()
# res2 = func('sochi')
# res2()
# res2()
# res2()
# res1()
# res3 = func('Kyev')
# res3()
# res3()
# res3()

# lambda(анонимная функция)


# print((lambda x, y: x + y)(1, 2))
#
# func = lambda x, y: x + y
# print(func(1, 2))
# print(func('a', 'b'))


# print((lambda x, y: x ** 2 + y ** 2)(2, 5))
# print((lambda x, y = 5: x ** 2 + y ** 2)(2, ))
# print((lambda x = 2, y = 5: x ** 2 + y ** 2)())
# print((lambda x = 2, y = 5: x ** 2 + y ** 2)(10, 20))
# print((lambda x = 2, y = 5: x ** 2 + y ** 2)(y = 10))


# print((lambda *args: args)(1, 2, 3, 4, 5))


# y = (
#     lambda x: x * 2,
#     lambda x: x * 3,
#     lambda x: x * 4,
# )
# for i in y:
#     print(i("abc__"))
#


# def outer(n):
#     def inner(x):
#         return x + n
#
#     return inner
#
#
# f = outer(5)
# print(f(10))
#
#
# def outer1(n):
#     return lambda x: x + n
#
#
# f1 = outer1(5)
# print(f1(10))
#
# outer2 = lambda n: lambda x: x + n
#
# f2 = outer2(5)
# print(f2(10))
#
# print((lambda n: lambda x: x + n)(5)(10))


# print((lambda x: lambda y: lambda z: x + y + z) (2)(4)( 6))


# def func(item):
#     return item[1]


# d = {'b':3, 'c': 1, 'a': 2}
# print(d)
# lst = list(d.items())
# print(lst)
# lst.sort(key=lambda i: i[1])
# # lst.sort(key=func)
# print(lst)
# d1 = dict(lst)
# print(d1)


# player = [
#     {'name':'Anton', 'last name': 'Bipykov', 'rating': 9},
#     {'name':'Aleksey', 'last name': 'Bodny', 'rating': 10},
#     {'name':'Fedor', 'last name': 'Sidorov', 'rating': 4},
#     {'name':'Mihail', 'last name': 'Semenov', 'rating': 6},
# ]
# res = sorted(player, key=lambda i: i['last name'])
# print(res)
# res = sorted(player, key=lambda i: i['rating'], reverse=True)
# print(res)


# a =[
#     lambda x, y: x + y,
#     lambda x, y: x - y,
#     lambda x, y: x * y,
#     lambda x, y: x / y,
#     lambda x, y: x // y,
#     lambda x, y: x % y,
# ]
#
# print(a[0](5, 2))
# print(a[1](5, 2))
# print(a[2](5, 2))
# print(a[3](5, 2))
# print(a[4](5, 2))
# print(a[5](5, 2))


# d = {
#     1: lambda: print("Понедельник"),
#     2: lambda: print("Вторник"),
#     3: lambda: print("Среда"),
#     4: lambda: print("Четверг"),
#     5: lambda: print("Пятница"),
#     6: lambda: print("Суббота"),
#     7: lambda: print("Воскресенье"),
# }
#
# d[6]()


# print((lambda a, b: a if a > b else b)(15, 23))


# print((lambda a, b, c: a if (a < b and a < c) else (b if b < c else c))(18, 19, 17))


# f = open(r'C:\Users\User\PycharmProjects\pythonProject1\test.txt, mode= 'r')
# f = open('test.txt', 'r')
# print(*f)
# print(f)
# f.close()
# print(f.close)
# print(f.mode)
# print(f.name)
# print(f.encoding)


# f = open('test.txt', 'r')
# print(f.read(3))
# print(f.read())
# f.close()

# f = open('test1.txt', 'r')
# #print(f.read())
# print(f.readline())
# print(f.readline(9))
# print(f.readline())
# f.close()


# f = open('test1.txt', 'r')
# print(f.readlines(16))
# print(f.readlines())
# f.close()

# f = open('test1.txt', 'r')
# count = 0
# for line in f:
#     print(line)
#     count += 1
# f.close()
# print("count =", count)  # подсчитывает количество строк в файле = 3


# f = open("xyz.txt", "w")
# f.write("Hello\nWorld\n")
#
# f.close()


# f = open("xyz.txt", "a")
# f.write("New text.\nOpen text in Explorer")
# f.close()
#
#
# f = open("test.txt", "a")
# f.write("This is a factor")
# f.close()


# f = open("xyz.txt", "w")
# line = ['This is line 1\n', 'This is line 2']
# f.writelines(line)
# f.close()


# class Stack:
#     def __init__(self):
#         print("Hi!")
#
# stackObject = Stack()


# class Stack:
#     def __init__(self):
#         self.__stacklist = [] # инкапсуляция - нельзя переменную увидеть из вне
# stackObject = Stack()
# print(len(stackObject.stacklist)) # выход - AttributeError


# class Stack:
#     def __init__(self):
#         self.__stacklist = []
#
#     def push(self, value):
#         self.__stacklist.append(value)
#
#     def pop(self):
#         value = self.__stacklist[-1]
#         del self.__stacklist[-1]
#         return value
#
#
# stackObject = Stack()
#
# stackList.push(3)
# stackList.push(2)
# stackList.push(1)
#
# print(stackList.pop())
# print(stackList.pop())
# print(stackList.pop())


# class Stack:
#     def __init__(self):
#         self.__stacklist = []
#
#     def push(self, val):
#         self.__stacklist.append(val)
#
#     def pop(self):
#         value = self.__stacklist[-1]
#
#     del self.__stacklist[-1]
#     return val
#
#
# stackObject1 = Stack()
# stackObject2 = Stack()
#
# stackObject1.push(3)
# stackObject2.push(stackObject1.pop())
# print(staclObject2.pop())


# for i in range(5):
#     nam = int(input())
#     nam1 = int(input())
#
#     print("Разность: ", nam - nam1)
#
# print("Вызов завершён")


# a = int(input("Введите числитель: "))  #-------------------------------- Программа при делении на 0 делить нельзя.
# b = int(input("Введите знаменатель: "))
# print('Результат : ', a/b if b else 'На ноль делить нельзя!!!')


# try:
# 	n = int(input("введите делимое : "))  #---------------------------------- программа с использованием исключений
# 	m = int(input("введите делитель : "))
# 	print("результат : ", n / m)
# except (ValueError, ZeroDivisionError):
# 	print("На ноль или строки вводить или делить нельзя")
# else:
# 	print("Всё нормально вы ввели : ", n, "и", m)
# finally:
# 	print("конец программы")


# n = input("введите число : ") # программа складывае равные по типу данных или конкатенация строк, строк+числа
# m = input("введите число : ")
#
# try:
#     n = int(n)
#     m = int(m)
# # print(int(n) + int(m))
# except ValueError:
#     n = str(n)
# # print(str(n) + str(m))
# finally:
#     print("программа завершилась", n + m)
#
#
# i = 1 # программа выводит только чётные числа в диапазоне от 1 до 20
# while i <= 20:
#     if i % 2 == 0:
#         print("i = ", i)
#     i += 1


# 25.11.2023 -------------------------------

# for i in range(3):
#     print(i)
#     if i == 1:
#         break
#     else:
#         print('done')

# for i in range(1):
#     print("+++ i  =", i)
#     for j in range(2):
#         print("----- j =", j)

# w = int(input("Введите ширину прямоугольника: "))  # программа вывода прямоугольника
# h = int(input("Введите высоту прямоугольника: "))
# for i in range(h):
#     for j in range(w):
#         if i == 0 or i == h - 1 or j == 0 or j == w - 1:
#             print("*", end="")
#         else:
#             print(" ", end="")
#     print()

# nums = [letter * 2 for letter in "Banana"]

# nums = [i for i in range(30) if i % 2 == 0] # Выводит чётные числа
# print(nums)

# Список

# nums = [8, 3, 9, 4, 1, "one"]
# print(nums)
# print(type(nums))
# print(nums[-2])
# # print(nums[0])
#
# nums[1] = 256
# print(nums)
# nums[3] += 100
# print(len(nums))
# for i in range(len(nums)):
#     print(nums[i] + 2)

# for i in range(1, 10):  # Таблица умножения
#     for j in range(1, 10):
#         print(i * j, end="\t")
#     print("\n")

# s = []
# print(s)
#
# b = list()
# print(b)  #  досмотреть и дописать 11:10 время

# a = [0 for _ in range(5)]  # нижнее подчёркивание это зарезервированное имя
# print(a)
# b = [_ for _ in range(5)]
# print(b)

# n = 5
# b = [i ** 2 for i in range(1, n + 1)]
# print(b)

# a, b = [1, 2, 3], [4, 5]
# c = a + b
# print(c)
# d = b * 3
# print(d)

# a = [0] * int(input("введите количество элементов списка: "))
# print(a)
# for i in range(len(a)):
#     a[i] = input("-> ")
# print(a)

# a = [input(">->-> ") for i in range(int(input("n = ")))]
# print(a)
#
# for i in range(1, len(a)):
#     if a[i] > a[i - 1]:
#         print(a[i], end="")

#  26.11.2023 ---------------

# a = [1, 2, 3, 4, 5, 6, 7]
# # print(a)
# # # a[0], a[1] = a[1], a[0]
# # print(a)
# # print(a[3:])
# # print(a[::2])
# a[1:3] = [0, 0, 0, 0]
# print(a)

# s = [5, 9, 3, 7, 1, 8]
# s.append(99)
# print(s)
# s.extend([1, 2, 3])
# print(s)
# s.insert(3, 100)
# print(s)
# s.extend('add')
# print(s)

# s = []
# n = int(input("Кол-во эл. списка: "))
# for num in range(n):
#     x = int(input("Введите число: "))
#     s.insert(0, x)
# print(s)

# задача выводит числа кратные 3
# s = []
# n = int(input("Кол-во элементов: "))
# for num in range(n):
#     x = int(input("Введите число кратное 3: "))
#     if x % 3 == 0:
#         s.append(x)
#     else:
#         print("Число не кратно 3: ")
# print(s)

# a = [5, 9, 2, 1, 4, 3, 2, 4]
# b = [4, 2, 1, 3, 7]
# c = []
# for i in a:
#     for j in b:
#         if i in c:
#             continue
#         if i == j:
#             c.append(i)
#             break
#
# print(c)

# a = [1, 2, 3]   #  сложить два списка и записать результат в с значение индексов 1+1; 2+2 ...
# b = [11, 22, 33]
# c = []
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# print(c)

# a = [1, 2, 3, 44, 55]
# b = [11, 22, 33]
# c = []
#
# if len(a) > len(b):
#     a, b = b, a
# for i in range(len(a)):
#     c.append(a[i])
#     c.append(b[i])
# for i in range(len(a), len(b)):
#     c.append(b[i])

# if len(b) > len(a):
#
#     for i in range(len(a)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(a), len(b)):
#         c.append(b[i])
# else:
#     for i in range(len(b)):
#         c.append(a[i])
#         c.append(b[i])
#     for i in range(len(b), len(a)):
#         c.append(a[i])
# print(c)

#
# s = [5, 9, 3, 7, 1, 8, 9, 9]
# print(s)
# s.remove(9)
# print(s)

# n = ......  #  дописать 12:40 - 12:50

# s = [5, 9, 3, 7, 9, 1, 8, 9]
# print(s)
# num = s.count(9)
# # print(num)
#
# ind = s.index(9) #  возвращает индекс первого искомого элемента
# print(ind)
# ind = s.index(9, 5)
# print(ind)

# a = [1, 3, 5, 6, 2, 4, 6, 1, 2, 7]
# b = []
# for i in a:
#     if i != a[0. i]:
#         b.append(i)
#         break
# print(b)


#  02.12.2023____------------------
# a = [1, 2, 3]
# b = a.copy()
# print("a =",a)
# print("b =",b)
#
# a.append(20)
# print("a =",a)
# print("b =",b)
# b.append(120)


# a = [5, 4, 1, 2, 3]
# print(a)
# # a.reverse()
# # print(a)
#
# # a.sort()
# # print(a)
# a.sort(reverse=True)
# print(a)


# b =["Виталий","Сергей","Александр","Анна"]
# b.sort(key=len, reverse=True)
# print(b)

# a = [5, 4, 1, 2, 3]
# print(a)
# a.sort()
# print(a)

# sort = sorted(a)
# print(sort)

#  Генерация случайных данных  ----->----------->-------------->------------->------------->


# print(random.random())
# print(random.randint(3, 9))
# print(random.randrange(3, 9))
#
# print(round(random.uniform(10.5, 25.5), 2))

# city_list = ['Москва', 'Новосибирск', 'Воронеж', 'Сочи', 'Екатеринбург']
# print(random.choice(city_list))
# print(random.choices(city_list, k=3))
# random.shuffle(city_list)
# print(city_list)


# s = [55, 66, 77, 88, 99, 9, 8, 7, 6, 5, 4, 1, 2, 3]
# print(random.choice(s))
# print(random.choices(s, k=5))

# lst = [5, 4, 3, 2, 1]
# print(len(lst))
# print(sum(lst))
# print(min(lst))
# print(max(lst))

# Задача --------------------------------

# import random
# mas = [random.randint(0, 20) for i in range(10)]
# print(mas)

# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# mas_ = max(mas)
# print(mas_)
# mas.remove(mas_)
# mas.insert(0, mas_)
# print(mas)  #  вариант 1 программа работает

# import random
# mas = [random.randint(0, 100) for i in range(10)]
# print(mas)
# max_ = max(mas)
# print(max_)
# mas.remove(max_)
# mas.insert(0, max_)
# print(mas)    # вариант 2 программа работает

#  Перемена--------------------------------
# Задача : программа находит мин значение и выводит в новый список с удалением других объектов впереди себя
# import random
#
# lst = [random.randint(0, 100) for i in range(10)]
# print(lst)
#
# min_ch = min(lst)
# print("min =", min_ch)
#
# ind_min = lst.index(min_ch)
# print("index min =", ind_min)
#
# del lst[: ind_min]
# print(lst)
# print(lst(ind_min))  # перепроверить

# lst = [5]
# print(lst)
# if not lst:
#     print("Список пуст")
# else:
#     print("В списке есть элементы")

# import random
#
# n1 = int(input("Введите размер первого списка: "))
# n2 = int(input("Введите размер второго списка: "))
#
# a = [random.randint(0, 10) for i in range(n1)]
# b = [random.randint(0, 10) for j in range(n2)]
# print("Первый список: ", a)
# print("Второй список: ", b)
# c = a + b
# print("Третий список: ", c)
# d = []
# for element in a:
#     if element not in d:
#         d.append(element)
# for element in b:
#     if element not in d:
#         d.append(element)
# print("Элементы обоих списков без повторений: ", d)
# c = []
# for i in a:
#     if i in b and i not in c:
#         c.append(i)
# print("Элементы общие для обоих списков: ", c)

# c = [min(a), min(b), max(a), max(b)]
# print(c)    # задача работает

#  ----- Домашняя работа от 02,12,2023


# import random
#
# print(random.sample(range(1, 10+1), 10))

# a = [random.randint(0, 10) for i in range(10)]
# b = []
# for element in a:
#     if element not in b:
#         b.append(element)
# print(b)

# import random
#   a = [random.randint(1, 10) for i in range(10)]
# for v in range(1, 10):
#     v = 2 ** v
#     b = list(random_range(v))
#     print("Need", v, "found", len(set(b)), "(min,max)", (min(b), max(b)))
# print("", b)
# print()

# m = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
# ]
# # m = ["Hello", "World"]
# print(m)
# # print(len(m))
# # print(m[1][2])
# print()
# # for row in range(len(m)):
# #     for col in range(len[row]):
# #         print(m[row][col], end="\t")
# #         print()
# for row in m:
#     for x in row:
#         print(x, end="\t")
#     print()


# Домашняя работа от 04.02.2024
# import os
#
# dir_name = 'Work'
# objs = os.listdir(dir_name)
# print(objs)
#
# for obj in objs:
#     p = os.path.join(dir_name, obj)
#     #print(p)
#     if os.path.isfile(p):
#         print(f"{obj} - file - {os.path.getsize(p)} bytes")
#     elif os.path.isdir(p):
#         print(f"{obj} - dir")


# 10.02.2024--------------------------------------------------------
#  в классе могут быть свойства (поля, переменные)
#  методы(функции). Имя класса пишется в верхнем регистре
#  пропускаем 2 пустых линии.
# class Point:
#     x = 1
#     y = 1
#
#     def set_coord(self, x, y):
#         self.x = x
#         self.y = y
#         print(self.__dict__)
#
# p1 = Point()
# # p1.x = 5
# # p1.y = 24
# # print(p1.x)
# # print(p1.y)
# # print(p1.__dict__)
# # print(id(p1))
# p1.set_coord(5, 24)
# Point.set_coord(p1, 5, 24)
#
#
# p2 = Point()
# # p2.x = 10
# # print(p2.x)
# # print(p2.y)
# # print(p2.__dict__)
# # print(id(p2))
# #
# # print(id(Point))
# p2.set_coord(10, 30)
#
# # 10:36-- дописать
# # 10.57 -- продолжим --------------------------------

#  задача ---------------------------------------------

# class Human():
#     name = "name"
#     birthday = "00.00.0000"
#     phone = "00-00-00"
#     country = "country"
#     city = "city"
#     address = "street, house"
#
#     def print_info(self):
#         print(" Персональные данные ".center(40, "*"))
#         print(f"Имя: {self.name}\nДата рождения: {self.birthday}\nНомер телефона: {self.phone}\n"
#               f"Страна: {self.country}\nГород: {self.city}\nДомашний адрес: {self.address}")
#         print("=" * 40)
#
#     def input_info(self, first_name, birthday, phone, country, city, address):
#         self.name = first_name
#         self.birthday = birthday
#         self.phone = phone
#         self.country = country
#         self.city = city
#         self.address = address
#
#     def set_address(self, address): # Устанавливает замену адрессса
#         self.address = address
#
#     def get_address(self): # получаем адресс
#         return self.address
#
#     def __set_name__(self, name): # Устанавливаем имя
#         self.name = name
#
#     def get_name(self): # Получаем имя
#         return self.name
#
#
# h1 = Human()
# h1.print_info()
# h1.input_info("Юля", "23.05.1986", "45-46-98", "Россия", "Москва", "Чистопрудный бульвар, 1A")
#
# h1.print_info()
# h1.set_address("ул.Ленина, 56")
# print(h1.get_address())
# h1.__set_name__("Юлия")
# print(h1.get_name())

# ----------------------------------------------------------------
# Задача

# class Person:
#     skill = 10  # Статическое свойство(имеют первоначальные значения)
#     count = 0  # считает количество экземпляров класса
#
#     # name = ""
#     # surname = ""
#
#     def __init__(self, name, surname):
#         self.name = name  # Динамические свойства
#         self.surname = surname
#         #print("Иннициализатор класса", self)
#         # self.count += 1 # обращаться к статическим свойствам через экземпляр класса
#         Person.count += 1 # обращаться к статическим свойствам через Имя класса
#
#     # def __del__(self):
#     #     print("Удаления экземпляра: ", self)
#     #
#     # def print_info(self):
#     #     print("Данные сотрудники: ", self.name, self.surname)
#     #
#     # def add_skill(self, k):
#     #     self.skill += k
#     #     print("Квалификация сотрудника: ", self.skill, end="\n\n")
#
#
# p1 = Person("Виктор", " Резник")
# # p1.print_info()
# # p1.add_skill(3)
# # del p1
# # p1 = 5
# print(p1.count)
#
# p2 = Person("Анна", "Долгих")
# # p2.print_info()
# # p2.add_skill(2)
# print(p2.count)
# print(Person.count)

# ------------------------------------------------------------------------------------------------
# Задача

# class Robot:
#     k = 0
#
#     def __init__(self, name):
#         self.name = name
#         print("Инициализация робота: ", self.name)
#         Robot.k += 1
#
#     def __del__(self):
#         print(self.name, "выключается")
#
#         Robot.k -= 1
#
#         if Robot.k == 0:
#             print(self.name, "был последним")
#         else:
#             print(self.name, "был последним")
#
#     def sey_hi(self):
#         print("Приветствую! Меня зовут: ", self.name)
#
#
# droid1 = Robot('R2-D2')
# droid1.sey_hi()
# print("Численность роботов: ", Robot.k)
#
# droid2 = Robot('C-3PO')
# droid2.sey_hi()
# print("Численность роботов: ", Robot.k)
#
# droid3 = Robot('S-9PO')
# droid3.sey_hi()
# print("Численность роботов: ", Robot.k)
#
# print("\nЗдесь роботы могут проделать какую-то работу\n")
#
# print("Роботы закончили свою работу. Давайте их выключим.")
# del droid1
# del droid2
# del droid3
#
# print("Численность роботов: ", Robot.k)


# 18.02.2024-------------------------------------------------------------------------------------------

# Задача она же и домашняя, нужно будет добавить в двух вариантах прорерти и гет и сет

# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = 'RUB'
#     suffix_usd = 'USD'
#     suffix_eur = 'EUR'
#
#     def __init__(self, surname, num, percent, value=0):
#         self.surname = surname
#         self.num = num
#         self.percent = percent
#         self.value = value
#         print(f"Счет #{self.num} принадлежащий {self.surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет #{self.num} принадлежащий {self.surname} был закрыт.")
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def add_money(self, val):
#         self.value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         uer_val = Account.convert(self.value, Account.rate_eur)
#         print(f"Состояние счёта: {uer_val} {Account.suffix_eur}")
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.value} {Account.suffix}")
#
#     def edit_owner(self, surname):
#         self.surname = surname
#
#     def add_percent(self):
#         self.value += self.value * self.percent
#         print("Проценты были успешно начислены")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.value:
#             print(f"К сожалению у вас нет {val} {Account.suffix}")
#         else:
#             self.value -= val
#             print(f"{val} {Account.suffix} было успешно снять!")
#         self.print_balance()
#
#     def print_info(self):
#         print('Информация о счете:')
#         print("-" * 20)
#         print(f"#{self.num}")
#         print(f"Владелец: {self.surname}")
#         self.print_balance()
#         print(f"Проценты: {self.percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account("Долгих", "12345", 0.03, 1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# Account.set_usd_rate(2)
# Account.set_eur_rate(3)
# print()
# acc.convert_to_usd()
# acc.convert_to_eur()
# acc.edit_owner("Дюма")
# acc.print_info()
# print()
# acc.add_percent()
# print()
# acc.withdraw_money(100)
# print()
# acc.withdraw_money(3000)
# print()
# acc.add_money(5000)
# print()
# acc.withdraw_money(3000)


# @property
# def fio(self):
#     return self.__fio
#
#
# @fio.setter
# def fio(self, fio):
#     self.verify_fio(fio)
#     self.__fio = fio
#
#
# @property
# def old(self):
#     return self.__old
#
#
# @old.setter
# def old(self, old):
#     self.verify_old(old)
#     self.__old = old
#
#
# @property
# def password(self):
#     return self.__password
#
#
# @password.setter
# def password(self, ps):
#     self.verify_ps(ps)
#     self.__password = ps
#
#
# @property
# def weight(self):
#     return self.__weight
#
#
# @weight.setter
# def weight(self, w):
#     self.verify_weight(w)
#     self.__weight = w
