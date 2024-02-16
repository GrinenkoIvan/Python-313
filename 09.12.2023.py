# ---------- Домашняя работа от 09.12.2023, случайные списки кортежа от 0 до 5 и от -5 до 0,
#сложить оба картежа и вывести в ответ сколько выпадает случайных чисел 0.-------------------
# Вариант

# import random
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