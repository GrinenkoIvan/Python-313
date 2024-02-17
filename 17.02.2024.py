# Классная работа

# class Point:
#     __slots__ = ["__x", "__y", "z"]
#     def __init__(self, x, y):
#         self.__x = self.__y = 0
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#
#
#     def __check_value(c):
#         if isinstance(c, int) or isinstance(c, float):
#             return True
#         return False
#
#     def get_coord(self):  # получить
#         return self.__x, self.__y
#
#     def set_coord(self, x, y):  # установить
#         # if (isinstance(x, int) or isinstance(x, float)) and (isinstance(y, int) or isinstance(y, float)):
#         if Point.__check_value(x) and Point.__check_value(y):
#             self.__x = x
#             self.__y = y
#         else:
#             print("Координаты должны быть числами!")
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#     def set_x(self, x):
#         if Point.__check_value(x):
#             self.__x = x
#         else:
#             print("Координата", x, "должна быть числом")
#
#
#     def set_y(self, y):
#         if Point.__check_value(y):
#             self.__y = y
#         else:
#             print("Координата", y, "должна быть числом")
#
#
# p1 = Point(5, 10)
# p1.z = 1
# print(p1.z)
# p1 = set_x(40.9)
# p1 = set_y(40.7)
# print(Point.__check_value(8))
# print(p1.get_coord())
# p1.set_coord(100, 200)
# print(p1.get_coord())
# print(p1.x, p1.y)
# p1.x = 100
# p1.y = 'abc'
# print(p1.x, p1.y)
# print(p1.__dict__)
#print(Point.__dict__)
# print(p1._Point__x, p1._Point__y)
# p1._Point__x = 111
# print(p1.__dict__)

# ----------------------------------------------------------------

# class Point:
#     def __init__(self, x, y):
#         self.__x = x
#         self.__y = y
#
#     def get_x(self):
#         return self.__x
#
#     def get_y(self):
#         return self.__y
#
#     def set_x(self, x):
#         self.__x = x
#
#     def set_y(self, y):
#         self.__y = y
#
#
# p1 = Point(5, 10)

# ----------------------------------------------------------------

# class Tools:
#     @staticmethod
#     def maximum(my_list):
#         return max(my_list)
#
#     @staticmethod
#     def minimum(my_list):
#         return min(my_list)
#
#     @staticmethod
#     def middle(my_list):
#         return sum(my_list) / len(my_list)  # среднее арифметическое
#
#     @staticmethod
#     def factorial(number):
#         if number == 1:
#             return 1
#         else:
#             return Tools.factorial(number - 1) * number
#
#
# print(f'Максимальное число: {Tools.maximum([3, 5, 7, 9])}')
# print(f'Минимум число: {Tools.minimum([3, 5, 7, 9])}')
# print(f'Среднее арифметическое: {Tools.middle([3, 5, 7, 9])}')
# print(f'Факториал числа {5}: {Tools.factorial(5)}')

# ----------------------------------------------------------------

# from math import sqrt
#
#
# class Square:
#     count = 0
#
#     @staticmethod
#     def square_triangle1(a, b, c):
#         Square.count += 1
#         p = (a + b + c) / 2
#         return sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def square_triangle2(a, b):
#         Square.count += 1
#         return 0.5 * a * b
#
#     @staticmethod
#     def square_area(a):
#         Square.count += 1
#         return a * a
#
#     @staticmethod
#     def square_rectangle(a, b):
#         Square.count += 1
#         return a * b
#
#     @staticmethod
#     def get_count():
#         return Square.count
#
#
# print('Площадь треугольника по формуле Герона:', Square.square_triangle1(3, 4, 5))
# print('Площадь треугольника через основание и высоту:', Square.square_triangle2(6, 7))
# print('Площадь квадрата:', Square.square_area(7))
# print('Площадь прямоугольника:', Square.square_rectangle(2, 6))
# print('Количество подсчетов площади:', Square.get_count())


# from math import sqrt
#
#
# class Square:
#     __count = 0
#
#     @staticmethod
#     def square_triangle1(a, b, c):
#         Square.__count += 1
#         p = (a + b + c) / 2
#         return sqrt(p * (p - a) * (p - b) * (p - c))
#
#     @staticmethod
#     def square_triangle2(a, b):
#         Square.__count += 1
#         return 0.5 * a * b
#
#     @staticmethod
#     def square_area(a):
#         Square.__count += 1
#         return a * a
#
#     @staticmethod
#     def square_rectangle(a, b):
#         Square.__count += 1
#         return a * b
#
#     @staticmethod
#     def get_count():
#         return Square.__count
#
#
# print('Площадь треугольника по формуле Герона:', Square.square_triangle1(3, 4, 5))
# print('Площадь треугольника через основание и высоту:', Square.square_triangle2(6, 7))
# print('Площадь квадрата:', Square.square_area(7))
# print('Площадь прямоугольника:', Square.square_rectangle(2, 6))
# print('Количество подсчетов площади:', Square.get_count())

















