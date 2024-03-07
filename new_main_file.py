# name = "Ivan"  # инициализация переменной

# print("Hello,", name)

# age = 20.4 # float(вещественное число)
# print(age)
# text = "Hello"
# print(text)
# print(text + str(age))  # str(строка)
# print(type(age))  # числовое значение int - 20, float 20.4
# print(type(text))  # str - "Hello"
# a = True  # bool - True, False
# print(a)
# a = False
# print(a)
# print(type(a))  # type(тип данных "bool")
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


# домашняя работа от 3,12,2023


# print("Введите номер фигуры согласно предложенному варианту: 1-прямоугольник, 2-треугольник, 3-круг")
# squar_figure = input("Выберите фигуру: ")
#
# if squar_figure == '1':
#     print("Длины сторон прямоугольника:")
#     a = float(input("a = "))
#     b = float(input("b = "))
#     print("Площадь прямоугольника = ", (a * b))
# elif squar_figure == '2':
#     print("Длины сторон треугольника:")
#     a = float(input("a = "))
#     b = float(input("b = "))
#     s = (a * b) / 2
#     print("Площадь треугольника = ", s)
# elif squar_figure == '3':
#     r = float(input("Радиус круга R = "))
#     s = (math.pi * r ** 2)
#     print("Площадь круга = ", s)
# else:
#     print("Ошибка ввода")


# square = input("Введите число для определения площади фигуры: 1- прямоугольник ,2- треугольник, 3- круг")
#
# pw = int(input("Основание прямоугольника: "))
# ph = int(input("Высота прямоугольника: "))
# ps = pw * ph
# print("Площадь прямоугольника = ", ps)
# elif square == 2:
# tw = int(input("Введите значение основания: "))
# th = int(input("Введите значение высоты: "))
# ts = (tw * th) / 2
# print("Площадь треугольника = ", ts)

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


#  # 23.12.2023  Домашняя работа
#
# month = ["January", "February", "March"]
# total_sales = [52000.00, 51000.00, 48000.00]
# prod_cost = [46800.00, 45900.00, 43200]
#
# for sales, costs, m in zip(total_sales, prod_cost, month):
#     profit = sales - costs
#     print("Чистая прибыль в :", m, "=", profit)

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
# player.sort(key=lambda i: i.lower())
# print(res)


# import fitz  # календарь на 3 года, нужно исправить
# import calendar
# import sys
#
# assert len(sys.argv) == 2, "need start year as the one and only parameter"
#
# startyear = sys.argv[1]
# assert startyear.isdigit(), "year must be positive numeric"
# startyear = int(startyear)
# assert startyear > 0, "year must be positive numeric"
#
# doc = fitz.open()
# cal = calendar.LocaleTextCalendar(locale="de")  # choose your locale
# w, h = fitz.PaperSize("a4-l")  # get sizes for A4 landscape paper
#
# txt = cal.formatyear(startyear, m=4)
# doc.insertPage(-1, txt, fontsize=12, fontname="Courier", width=w, height=h)
#
# txt = cal.formatyear(startyear + 1, m=4)
# doc.insertPage(-1, txt, fontsize=12, fontname="Courier", width=w, height=h)
#
# txt = cal.formatyear(startyear + 2, m=4)
# doc.insertPage(-1, txt, fontsize=12, fontname="Courier", width=w, height=h)
#
# doc.save("Kalender.pdf", garbage=4, deflate=True)
#
# print("Kalender", txt, fontsize=12, fontname="Courier",)


# n = int(input())
# l = [input().split() for i in range(n)]
# mean = sum([int(i[-1]) for i in l])//n
# for i in sorted(l):
#     if int(i[-1]) >= mean:
#         print(*i[:-1], mean)


# 13.01.2024--------------------------------

# map(func, *iterables)

# def mult(t):
#     return t * 2
# lst1 = [2, 8, 12, -5, -10]
#
# lst2 = list(map(lambda t: t * 2, lst1))
#
# # lst2 = list(map(mult, lst1))
# print(lst2)  # [4, 16, 24, -10, -20]

# t = (2.88, -1.75, 100.55)
# # t2 = tuple(map(lambda x: int(x), t))  # (2, -1, 100)
# t2 = tuple(map(int, t))
# print(t2)

# st = ['a', 'b', 'c', 'd', 'e']
# num = [1, 2, 3, 4, 5]
#
# res = list(map(lambda x, y: (x, y), st, num))
# print(res)

# l1 = [1, 2, 3]
# l2 = [4, 5, 6]
#
# res = list(map(lambda x, y: x + y, l1, l2))
# print(res)


# t = ('abcd', 'abc', 'asdfg', 'def', 'grt')
# t2 = tuple(filter(lambda s: len(s) == 3, t))
# print(t2)  # ('abc', 'def', 'grt')


# b = [66,90,68,59,76,60,88,74,81,65]
# res = list(filter(lambda s: s > 75, b))
# print(res)  # [90, 76, 88, 81]


# m = list(map(lambda x: x ** 2, filter(lambda x: x % 2, range(10))))
# print(m) #  [1, 9, 25, 49, 81]
# n = [x ** 2 for x in range(10) if x % 2]
# print(n)   [1, 9, 25, 49, 81]


# m = list(map(lambda x: x ** 2, filter(lambda x: x > 10 < 21, randint(10, 40))))
# print(m) # [1, 9, 25, 49, 81]

# import random
#
# my_list = [random.randint(1, 40) for i in range(20)]
#
# print(my_list)
# print(list(filter(lambda num: 10 <= num <= 20, my_list)))


# def hello():
#     return 'Hello , I am func "hello"'
#
#
# def super_func(func):
#     print('Hello , I am func "super_func"')
#     print(func())
#
#
# super_func(hello)  # Передача функции в другую функцию


# def hello():
#     return 'Hello , I am func "hello"'
#
# test = hello
# print(test())  # Ссылается на функцию, т.е на один объект памяти


# def my_decorator(func):
#     def wrap():
#         print("Код функции")
#         func()
#         print("Код после функции")
#
#     return wrap
#
#
# def func_test():
#     print('Hello, I am func "func_test"')
#
#
# test = my_decorator(func_test)
# test()


# def my_decorator(func):  # декорирующая функция
#     def wrap():
#         print("Код функции", "*" * 35)
#         func()
#         print("Код после функции", "*" * 35)
#
#     return wrap
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print('Hello, I am func "func_test"')
#
#
# func_test()


# test = my_decorator(func_test)
# test()


#  -------------------перемена----------------------


# def my_decorator(func):  # декорирующая функция
#     def wrap():
#         print("Код функции", "*" * 35)
#         func()
#         print("Код после функции", "@" * 35)
#
#     return wrap
#
# @my_decorator  # декоратор
# def func_test():  # декорируемая функция
#     print('Hello, I am func "func_test"')
#
# @my_decorator
# def hello():
#     print('Hello, I am func "hello"')
#
#
# func_test()
# hello()

# def hello(t):
#     return t * 2, 'Hello, I func "hello"'
#
#
# def super_func(func):
#     print('Hello, I func "super_func"')
#     print(func())
#
#
# super_func(hello)

# def func_test():
#     print('Hello, I am func "func_test"')  # допасать после перемены

# def bold(fn):
#     def wrap():
#         return "<b>" + fn() + "</b>"
#
#     return wrap
#
#
# def italic(fn):
#     def wrap():
#         return "<i>" + fn() + "</i>"
#
#     return wrap

#
# @bold
# @italic
# def hello():
#     return "text"
#
#
# print(hello())


# def cnt(fn):
#     count = 0  # Декоратор со счётчиком
#     def wrap():
#         nonlocal count
#         count = count + 1
#         fn()
#         print("Вызов функции: ", count)
#
#     return wrap
#
# @cnt # применяем декоратор с встроеным счётчиком
# def hello():
#     print("Hello")
#
#
# hello()
# hello()
# hello()


# def cnt(fn):
#     count = 0
#     def wrap(arg1, arg2):
#         nonlocal count
#          = count + 1
#         fn(arg1, arg2)
#         print("Вызов функции: ", count, "\n", )
#
#     return wrap
#
# @cnt
# def hello(a, b):
#     print("Hello ", a, " Hello", b)
#
#
#
# hello("Python", "JavaScript")
# hello("Python", "JavaScript")
# hello("Python", "JavaScript")
#
# # hello()
# # hello()  # дописать


# def args_decorator(fn):
#     def wrap(*args, **kwargs):
#         print("args", args)
#         print("kwargs", kwargs)
#         fn(*args, **kwargs)
#     return wrap
#
#
# @args_decorator
# def print_data(a, b, c, study="Python"):
#     print(a, b, c, "изучают", study, "\n")
#
#
# print_data("Борис", "Елизавета", "Светлана", study="JavaScript")
# print_data("Владимир", "Екатерина", "Виктор")

# def decor(agrs1, agrs2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(agrs1, x, agrs2, y, "=", end="")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма","+")
# def summa(a, b):
#     print(a + b)
#
#
# @decor("Разность: ", "-")
# def summa(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# summa(10, 7)


# def multiply(arg):
#     def test(fn):
#         def wrap(x):
#             return fn(x) * arg
#
#         return wrap
#
#     return test
#
#
# @multiply(3)
# def return_num(num):
#     return num
#
#
# print(return_num(5))


# a = [int(input('==>')) for _ in range(int(input('n =')))]
# print(a)
# for i in range(len(a)):
#     if i % 2 == 0:
#         print()


# import random
#
# my_list = [random.randint(1, 40) for i in range(20)]
#
# print(my_list)
# print(list(filter(lambda num: (num >= 10) and (num <= 20), my_list)))


# def decor(agrs1, agrs2):
#     def args_dec(fn):
#         def wrap(x, y):
#             print(agrs1, x, agrs2, y, "= ", end="")
#             fn(x, y)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма","+")
#
# a = [int(input('==>')) for _ in range(int(input('n =')))]
# def summa(a, b):
#
#     print(a + b)
#
#
# @decor("Разность: ", "-")
# def summa(a, b):
#     print(a - b)
#
#
# summa(5, 2)
# summa(10, 7)
#

# def decor(func):
#
#
#
# numbers = [int(input('->')) for _ in range(int(input('n = ')))]
# total = 0
# for number in numbers:
#     total += number
# print(total)

# from statistics import mean
#
#
# def average(function):
#
#     def inner(*args):
#         function(*args)
#         print('Средне арифметическое чисел', args, '=', mean(args))
#
#     return inner
#
#
# @average
# def sum_of_numbers(*args):
#     print('Сумма чисел', args, '=', sum(args))
#     return args
#
#
# sum_of_numbers([int(input('->')) for _ in range(int(input('n = ')))])


# 14.01.2024 --------------------------------


# print(int('100', 2)) # 4
# print(int('100', 4)) # 64
# print(int('100', 10)) # 100
# print(int('100', 16)) # 265
# print(bin(18)) # 0b10010
# print(oct(18)) # 0o22
# print(hex(18)) # 0x12


# q = 'Pyt'
# w = "hon"
# e = q + w
# print(e)
# # print(e * 3)
# # print('y' in e)
# # print(e[-6])
# # print(e[:4])
# # print(e[2:])
# # print(e[::-1])
#
# e = e[:3] + 't' + e[4:]
# print(e)


# def changeCharToStr(s, c_old, c_new):  # Функция заменяет буква "N"/"P"
#     s2 = ""
#     i = 0
#
#     while i < len(s):
#         if s[i] == c_old:
#             s2 = s2 + c_new
#         else:
#             s2 += s[i]
#         i += 1
#     return s2
#
#
# str1 = "Я изучаю Nython. Мне нравиться Nython. Nython очень интересный язык программирования"
# str2 = changeCharToStr(str1, "N", "P")
# print("str1 = ", str1)
# print("str2 = ", str2)

# print("Привет")
# print(u"Привет")


# dir_name = " my_doc"
# file_name = "data.txt"
# print(fr"home\{dir_name}\{file_name}")
# print("home\\" + dir_name + "\\" + file_name)


# s = """
# Многострочный
# текст
# """
#
# s1 = '''
# Многострочный текст
# '''
# print(s)
# print(s1)


# def square(n):
#
#     """Принимает число n,  возвращает квадрат n"""
#     return n ** 2
#
#
#
# print(square(2))
# print(square.__doc__)
# print(sum.__doc__)
# print(min.__doc__)
# print(len.__doc__)


# from math import pi

# def cylinder(r,h):   # документация
#
#     """
#     Вычисляет площадь цилиндра.
#
#     Вычисляет площадь цилиндра на основании заданной высоты и радиуса основания
#
#     :param r: положительное число, радиус основания цилиндра
#     :param h: положительное число, высота цилиндра
#     :return: положительное число, площадь цилиндра
#     """
#     print("Hello")
#     return 2 * pi * r * (r + h)
#
#
# print(cylinder(2, 4))
# print(cylinder.__doc__)


# print(ord("a")) # 97
# print(ord("й")) # 1081


# while True:
#     n = input("->")
#     if n != "-1":
#         print(ord(n))
#     else:
#         break

# print(chr(1104))


# s = "Test string for me" # программа находит коды, складывает, находит равные по коду, добавляет в начало списка,
# находит кол-во похожих кодов и выводит значение на уменьшение arr = [ord(x) for x in s] print("ASCII коды: ",
# arr) arr = [int(sum(arr) / len(arr))] + arr print("Среднее арифметическое: ", arr) arr += [ord(x) for x in input(
# "->")[:3] if ord(x) not in arr] print(arr) print(arr.count(arr[-1]) - 1), arr.sort(reverse=True) print(arr)


# print(chr(122))
# print(chr(1048))
# print(chr(8364))

# print(ord("a"), " = (a)")  # a = 97

# 20.01.2024------------------------------

# from random import randint
#
# SHORTEST = 7
# LONGEST = 10
# MIN_ASCII = 33
# MAX_ASCII = 126
#
#
# def random_password():    # сформировать пароль из случайных букв и цифр
#     random_length = randint(SHORTEST, LONGEST)
#     result = ""
#     for i in range(random_length):
#         result += chr(randint(MIN_ASCII, MAX_ASCII))
#     return result
#
#
# print("Ваш случайный пароль", random_password())


# s = "hello, WORLD! I am learning Python."
# print(s.capitalize()) # Hello, world! i am learning python.
# print(s.lower()) # hello, world! i am learning python.
# print(s.upper()) # HELLO, WORLD! I AM LEARNING PYTHON.
# print(s.swapcase()) # HELLO, world! i AM LEARNING pYTHON.
# print(s.title()) # Hello, World! I Am Learning Python.
# print(s.casefold()) # hello, world! i am learning python.


# print(s) # print(s.count("WORLD")) # print(s.count("h", 1, -4))  #  возвращает кол-во точных вхождений подстроки в
# строку # print(s.find("Python1"))  # Ищет в строке заданную подстроку и вовращает её индекс, если совпадений не
# найдено то возвращает -1 # print(s.find("Python", 10, -20))  # Ищет в строке заданную подстроку и вовращает её
# индекс, если print(s.find("l"))  # Ищет в строке заданную подстроку и вовращает её индекс, если print(s.rfind("l"))
# Ищет в строке заданную подстроку и вовращает её индекс, если совпадений не найдено то возвращает -1 print(s.index(
# "l")) print(s.rindex("l"))

# задача на вывод двух слов с перестановкой местами в выводе
# _s = input("Введите строку из двух слов через пробел :") # один два
# first = _s[:_s.find(" ")]
# second = _s[_s.find(" ") + 1:]
# print(_s)
# print(first)
# print(second)
# print(second + " " + first)


# s = "hello, WORLD! I am learning Python."
# print(s)
# print(s.startswith("hello"))
#
# print(s.endswith("on."))
# print(s.endswith("lo", 3, 5))


# print("abc123".isalpha())
#
# print("abcABC".isalpha()) # определяет состоит ли строка только из букв # True
# print("".isalpha()) # False
# print('123'.isdigit()) # Проверяет наличие цифр в строке # True
# print('123'.isalnum()) #  определяет состоит ли строка только из букв и цифр # True
# print("abc".islower()) # определяет , являются ли буквенные символы строки строчными # True
# print("abcABC".islower()) # определяет , являются ли буквенные символы строки строчными # False
#
# print("!456A".isupper())  # определяет, является ли буквенные символы строки в верхнем регистре


# s = "hello, WORLD! I am learning Python."
# # print('py'.center(20, ">"))
#
# # print("     py".lstrip()) #  убирает пробельные символы слева от строки
# # print("py     ".rstrip()) # убирает пробельные символы справа от строки
# # print("       py     ".strip()) # убирает пробельные символы справа и слева от строки
#
# print("http://www.python.org".lstrip())  # http://www.python.org
# print("https://www.python.org".lstrip("/:pths").rstrip(".org"))  # www.python
# print("https://www.pythons.org".strip("/:pths.org")) # www.python

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# print(str1)
# print(str1.replace("Nython", "Python"))
# print(str1.replace("Nython", "Python", 2))

# перемена

# s = "hello, WORLD! I am learning Python."
# s1 = "-"
# seq = ("a", "b", "c")
# print(s1.join(seq))
# print("..".join(['1', '2']))  # объединение итерируемой последовательности (состоит из строковых значений)
# print(":".join("Hello"))

# s = "hello, WORLD! I am learning Python."
# # print(s.split())  #  ['hello,', 'WORLD!', 'I', 'am', 'learning', 'Python.']
# # print('www.python.org.ru'.split(".",2))  #  ['www', 'python', 'org.ru']
# # print('www.python.org.ru'.rsplit(".", 1))  # ['www.python.org', 'ru']
#
#
# a = input("-> ").split()
# print(a)


#  Задача------------------------

# a = input("Введите фамилию, имя, отчество : ").split()
# print(a[0], a[1][0] + "." + a[2][0] + ".")  # Выводит фамилию и инициалы через точку


# a = input("Введите кол-во символов кода : ").split()
# print(a)
#
# b = list(map(int, a))
# print(b)


# Регулятные выражения--------------------------------

# import re

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = r"\."
# print(re.findall(reg, s))  #  возвращает список , сож\держащий все совпадения с шаблоном регулятных выражений

# print(re.search(reg, s))  # возвращает первого совпаденния с шаблоном

# print(re.search(reg, s).span())
# print(re.search(reg, s).start())
# print(re.search(reg, s).end())
# print(re.search(reg, s).group())
# print(re.match(reg, s))

# print(re.split(reg, s))
# print(re.sub(reg,"!", s, 1))

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# # reg = r"[12][0-9][0-9][0-9]"
# reg = r"[А-я-Ёё]"

# print(re.findall(reg, s))
# print(ord('a'))
# print(ord('я'))
# print(ord('ё'))


# 21.01.2024---------------------------------------------------------

# import re

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта. 198765 Hello [-World]"
# reg = r"[a-zA-Z\]\[-]"
# print(re.findall(reg, s))

# st = "Час в 24-часовом формате от 00 до 23. 2021-06-10Е21:45. Минуты, в диапазоне от 00 до 59. 2021-06-15Т01:09."
# reg = r"[0-2][0-9]:[0-5][0-9]"
# print(re.findall(reg, st))

# st = "05-03-1987 # Дата рождения"
# # print("Дата рождения: ", re.sub(r"#.*", "", st))
# # print("Дата рождения: ", re.sub(r"#.*", ".", st).replace(r"-", "."))
# print("Дата рождения: ", re.sub(r"-", ".", re.sub(r"#.*", "", st)))
# st = '05-03-1987 # Дата рождения'
# print('Дата рождения:', re.sub(r'-', '.', re.search(r'\d{2}-\d{2}-\d{4}', st).group()))


# st = "autor=Пушкин А.С.; title = Евгений Онегин; price =200; year= 1831"
# req = r"\w+\s*=\s*\w+[^;]+"
# print(re.findall(req, st))


# st = "12 сентября 2021 года 245"
# req = r"\d{2,4}"
# print(re.findall(req, st))


# st = "+7 499 456-45-78, +74994564578, +7(499) 456 45 78, 74994564578"
# # req = r'\+?7\d{10}'
#
# print(re.findall(r"[+]?7\s?\d{3}\s?\d{3}-?\d{2}-?\d{2}", number)) # разобраться
# print(re.findall(req, st))

# def valid_login(name):
#     return re.findall(r"^[A-Za-z0-9_-]{6,16}$", name) # 6-16 англ.буквы_, -, [0-9], {6-16 символов}
#
#
# print(valid_login("Pyton_master"))
# print(valid_login("!!!Python"))


# print(re.findall(r"\w+", "12 + й"))
# print(re.findall(r"\w+", "12 + й", flags=re.ASCII))
# print(re.findall(r"\w+", "12 + й", flags=re.A))
# print(re.findall(r"\w+", "12 + й", re.A))


# text = "hello world"
# print(re.findall(r"\w\+", text, re.DEBUG))

# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = r'я'
# print(re.findall(reg, s, re.IGNORECASE))


# text = """
# one
# two
# """
# print(re.findall(r'one.\w+', text)) # one\ntwo
# print(re.findall(r'one.\w+', text, re.DOTALL))
# print(re.findall(r'one$', text))
# print(re.findall(r'one$', text, re.MULTILINE))
# print(re.findall(r"""[a-z.-]+@[a-z.-]+""", 'test@mail.ru', re.VERBOSE))


# text = """Python,
# python,
# PYTHON"""
# reg = "(?im)^python"  # i отменяет регистр, m- любое количество повторений
# print(re.findall(reg, text))
# data = '123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru'
# pattern = re.findall(r'[.\-\w]+@[.\w]+', data)
# print(pattern)

# tft = """JavaScript,
# HTML,
# CSS"""
# reg = "(&im)^javascript"
# print(re.findall(reg, tf))


# 27.01.2024 --------------------------------

# text = "<body>Пример жадного соответствия регулярных выражений</body>"
# print(re.findall("<.*?>", text))
#
# # *?, +?, ??
# # {m,n}?, {,n}?, {m,}?
#
# st = "12 сентября 2021 года 23554154564156"
# reg = r"\d{2,4}?"
# print(re.findall(reg, st))


# s = "<p>Изображение <img src='bg.jpg'> - фон страницы</p>"
# #reg = r'<img.*?>'
# reg = r'<img[^>]*>'
# print(re.findall(reg, s))

# s = "<p>Изображение <img alt='картинка' src = 'bg.jpg'> - фон страницы</p>"
# #reg = r'<img.*?>'
# reg = r'<img\s+[^>]*src\s*=\s*[^>]+>'
# print(re.findall(reg, s))

# text = "Python (в русском языке встречаются названия пито́н[16]или па́йтон[17]) — высокоуровневый язык " \
#        "программирования общего назначения с динамической строгой типизацией " \
#        "и автоматическим управлением памятью[18][19]."

# print(re.findall(r'\[\d+]', text))
# print(re.findall(r'\[.*?]', text))

# s = "Пётр , Ольга и Виталий отлично учаться!"
# reg = 'Пётр|Виктор|Ольга|Виталий'
# print(re.findall(reg, s))

# s = "int = 4, float = 4.0f, double = 8.0, float, int"
# # reg = r'\w+\s*=\s*\d[.\w]*'
# #reg = r'(?:int|float)\s*=\s*\d[.\w]*'  #  (?: - эта группирующая скобка является не сохраняющей )
# #reg = r'((int|float)\s*=\s*(\d[.\w]*))'  # [('int = 4', 'int', '4'), ('float = 4.0f', 'float', '4.0f')]
# #print(re.findall(reg, s))
# reg = r'\w+\s*=\s*\d[.\w]*'
# print(re.saearch(reg, s).group)


# s = '127.0.0.1'
# #s = '127.168.255.255'
# #reg = r'\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3}'  # ['127.168.255.255']
# reg = r'(?:\d{1,3}.){3}\d{1,3}' # ['127.168.255.255']
# print(re.findall(reg, s))


# s = "5 + 7*2 - 4"
# reg = r'\s*([+*-])\s*'
# print(re.split(reg, s))


# a = '28-08-2021'
# pattern = '(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-(19[0-9][0-9]|20[0-9][0-9])'
# print(re.findall(pattern, a))
# print(re.search(pattern, a).group())


# s = "Я ищу совпадения в 2024 году. И я их найду в 2 счёта."
# reg = r'([0-9]+)\s(\D+)'
# print(re.findall(reg, s))
# print(re.search(reg, s). group(0))
# m = re.search(reg, s)
# print(m[0])
# print(m[1])
# print(m[2])


# text = """
# Самара
# Москва
# Тверь
# Уфа
# Казань
# """
# count = 0
#
# def repl_find(m):
#     global count
#     count += 1
#     return f"<option value'{count}'>{m.group(1)}</option>\n"
#
#
# print(re.sub(r'\s*(\w+)\s*', repl_find, text))


# s = "<p>Изображение <img src='bg.jpg'> - фон страницы </p>"
# #reg = r"<img\s+[^>]*src\s*=(['\"])(.+?)\1>"
# reg = r"<img\s+[^>]*src\s*=(?P<q>['\"])(.+?)(?P=q)>"  # (?P<name>...)  (?P=name)
# print(re.findall(reg, s))


# s = "Самолёт прилетает 10/23/2024. Будем рады вас видеть после 10/24/2024."
# reg = r'(\d{2})/(\d{2})/(\d{4})'
# print(re.sub(reg, r'\2.\1.\3', s))


# s = "yandex.com.ru and yandex.ru"
# reg = r'(([a-z0-9-]{2,}\.)+[a-z]{2,4})'
# print(re.sub(reg, r"http://\1", s, re.IGNORECASE))


# 28.01.2024 -------------------------------- Рекурсия


# def elevator(n):
#     if n == 0:
#         print("Вы в подвале")
#         return
#     print(">>>", n)
#     elevator(n - 1)
#     print(n, end=" + ")  # 1 + 2 + 3 + 4 + 5 +
#
#
# n1 = int(input("На каком Вы этаже: ")) # 5
# elevator(n1)


# def sum_list(list):
#     res = 0
#     for i in list:
#         res += i
#     return res
#
#
# print(sum_list([1, 3, 5, 7, 9]))  # 25


# def sum_list(lst):
#     if len(lst) == 1:
#         return lst[0]
#     else:
#         return lst[0] + sum_list(lst[1:])
#
#
# print(sum_list([1, 3, 5, 7, 9]))


# def to_str(n, base):   #  n = 365
#     convert = "0123456789ABCDEF"
#     if n < base:  # 365 < 10
#         return convert[n]
#     else:
#         return to_str(n // base, base) + convert[n % base]
#
#
# print(to_str(365, 10)) # 365
# print(to_str(365, 2)) # 101101101
# print(to_str(365, 8)) # 555
# print(to_str(365, 16)) # 16D


# names = ['Adam', ['Bob', ['Chet', ['a', 'b'], ['c', 'd'], 'Cat'], 'Bard', 'Bert'], 'Alex', ['Bea', 'Bill'], 'Ann']
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
# def count_iten(lst):
#     count = 0
#     for item in lst:
#         if isinstance(item, list):
#             count += count_iten(item)
#         else:
#             count += 1
#     return count
#
#
# print(count_iten(names))


# def remove(text):
#     if not text:
#         return ""
#     if text[0] == "\t" or text[0] == " ":
#         return remove(text[1:])
#     else:
#         return text[0] + remove(text[1:])
#
#
# print(remove("Hello\tWorld "))


# Файлы ----------------------------------

# Текстрвые
# Бинарные

# f = open('test.txt', mode='r')
# print(f)

# Домашняя работа от 13.01.2024=====================================================================================
from statistics import mean


# def average(function):
#
#     def inner(*args):
#         function(*args)
#         print('Средне арифметическое чисел', args, '=', mean(args))
#
#     return inner
#
#
# @average
# def sum_of_numbers(*args):
#     print('Сумма чисел', args, '=', sum(args))
#     return args
#
#
# sum_of_numbers(2, 3, 3, 4)