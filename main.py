# print("Hello,", name)
import random

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

# Задача

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

# Домашняя работа от 12.11.2023 -- Пользователь вводит число/ программа выводит время года и месяц  #


# month = int(input("Введите месяц года (цифрой): "))
# if 1 <= month <= 2 or month == 12:
#     print("Это зима -", end=" ")
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

# anything = input("Tell me anything...")
# print("Hmm...", anything, "...Really?")

# leg_a = float(input("Input first leg length: "))
# leg_b = float(input("Input second leg length: "))
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


# password = "qwerty"
#
# match password:
#     case 'admin':
#         print("Администратор")
#     case "user":
#         print("Пользователь")
#     case _:
#         print("Логин не найден")

# day = 'вторник'
# time = 14
# match day:
#     case "понедельник" | "вторник" | "среда" | "четверг" | "пятница" if 9 <= time <= 13 or 15 <= time <= 16 :
#         print("Рабочий день")
#     case "суббота" | "воскресенье":
#         print("Выходной день")
#     case _:
#         print("Такого дня недели не существует или не рабочее время")

# a, b =  20, 30
#
# print(a if a < b else b)

# a, b = 20, 30
#
# print("a == b" if a == b else "a > b" if a > b else "b > a")

# a = 5
# b = 0
# print("на ноль делить нельзя " if b == 0 else a / b)
# print(a / b)

# try:
#     n = int(input("Ввести целое число: "))
#     print(n * 2)
#
# except ValueError:
#     print("Что то пошло не так")
#
# print("перешли на следующую строку")


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

#  циклы

# i = 0
# while i < 5:
#     print("i =", i)
#     i+=1


# i = 10
# while i > 0:
#     print("i =", i)
#     i -= 1


# i = 0
# while i <= 20:
#     print("i ", i)
#     i += 2

# i = 1
# while i <= 20:
#     if i % 2 == 0:
#         print(i)
#         i += 1

# n = int(input("Лоличество символов: "))
# i = 0
# while i < n:
#     print("*", end="")
#     i += 1

# n = int(input("Лоличество символов: "))
# print("*\n" * n)

# a = int(input("Ввести начало диапазона: "))
# b = int(input("Ввести конец диапазона: "))
# res = 0
# while a <= b:
#     if a % 2 != 0:
#         res += a
#     a += 1
# print(res)


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


# 19.11.2023


# n = input("Введите целое число: ")
#
# while type(n) != int and type(n) != float:
#     try:
#         if n // 1 == 0:
#         print("Чётное")
#     except ValueError:
#         print("Число не целое")
#         n = input("Введите целое число: ")
#     # finally:
#     #     print("Программа завершена", n)
#
# if n % 2 == 0:
#     print("Чётное")
# else:
#     print("Нечётное") # не работает

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


# Домашняя работа от 19.11.2023
# stat = 1
# while True:
#     n = int(input("Угадайте число от 1 до 100: "))
#     number = 55
#     if n < number:
#         print("Ваше предположение меньше, чем число.")
#     if n > number:
#         print("Ваше предположение больше, чем число.")
#     if n == 0:
#         print("Завершить программу.")
#         break
#     elif n == number:
#         print("Вы угадали загаданное число: ", number)
#         break
#     n += 1
#     stat += 1
# print("Количество попыток =", stat)
# работает-------------------------------------------------------------------------------------------
#


# i = 0
# while i < 10:
#     if i == 5:
#         break  # останавливает цикл
#     print(i, end=" ")
#     i += 1
# else:
#     print("\nЦикл окончен. i =", i)  # работает

# таблица умножения
# i = 1
# while i < 10:
#     j = 1
#     while j < 10:
#         print( i, "*", "=", i * j, end="\t\t")
#         j += 1
#     print()
#     i += 1

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
#     j = 16
#     if i % 2 == 0:
#         print("+" * 16)
#     else:
#         print("-" * 16)
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

# Домашняя работа от 19.11.2023

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
#
# print(a)

# n = list(range(21, 41))
# print(n)
# s = k = 0
# for i in range(len(n)):
#     if n[i] % 2 == 0:
#         k += 1
#     else:
#         s += n[i]
# print("sum нечётных элементов: ", s)
# print("count чётных элементов: ", k)

# n = list(range(21, 41))
# print(n)
# s = k = 0
# for i in n:
#     if i % 2 == 0:
#         k += 1
#     else:
#         s += i
# print("sum нечётных элементов: ", s)
# print("count чётных элементов: ", k)

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
#         if not even and current % 2:
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


#  Кортеж (tuple)

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

from random import randint

# s = tuple(input("->") for i in range(5))
# s = tuple(int(input("->")) for i in range(5))
# s = tuple(randint(0, 100) for i in range(5))
# print(s)


# s = tuple(2 ** i for i in range(1, 13))
# print(s)

# t1 = tuple("Hello")
# t2 = tuple("world")
# print(t1)
# print(t2)
# t3 = t1 + t2
# print(t3.count('l'))
# if 'e' in t3:
#     print(t3.index('e'))
#
# for i in t3:
#     print(i, end="")

# задача-----------

# def slicer(tpl, el):
#     if el in tpl:
#         if tpl.count(el) > 1:
#         # a = tpl.index(el)
#         # b = tpl.index(el, a+1)
#         # return tpl[a:b+1]      или .....
#             return tpl[tpl.index(el):tpl.index(el, tpl.index(el) + 1) + 1]
#         else:
#             return tpl[tpl.index(el):]
#
#     else:
#         return tuple()
#
# print(slicer((1, 2, 3), 8))
# print(slicer((1, 8, 3, 4, 8, 8, 9, 2), 8))
# print(slicer((1, 2, 8, 5, 1, 2, 9), 8))

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
# import random
# initial = tuple([random.randint(0, 5) for _ in range(10)])
# print(initial)
# other = tuple([random.randint(-5, 0) for _ in range(10)])
# print(other)
# upshot = initial + other
# print(upshot)
# print("0 = ", upshot.count(0))


# -------------Домашняя работа от 10.12.2023 , вывести статистику чачтотности чисел в кортеже----

# num = str(253523651)
# print(num)
# first = tuple(num)
# print(first)
# print(first.count(2))


# print("2 =", first.count(2))
# print("5 =", first.count(5))
# print("3 =", first.count(3))
# print("6 =", first.count(6))
# print("1 =", first.count(1))

# print("Вносим изменения")

# print("Склонированный репозиторий")


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


  # Словарь --------------



s = input("Введите строку: ")
count = 0
str_1 = set("уеэоаяюи")
for str_2 in s:
    if str_2 in str_1:
        count += 1
print("Количество гласных равно: ",(count))

