# def func(args):
#     if len(args) == 0:
#         let = 0
#         return let
#     elif args[0] > 0:
#         return func(args[1:])
#     else:
#         let = 1
#         return let + func(args[1:])
#
#
# print("n =", func([-2, 3, 8, -11, -4, 6]))

# вариант 2

# def func(a):
#     if not a:
#         return 0
#     else:
#         count = func(a[1:])
#         if a[0] < 0:
#             count += 1
#         return count
#
#
# lst = [-2, 3, 8, -11, -4, 6]
# print(func(lst))
