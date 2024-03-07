#  13.01.2024 Домашняя работа

def decorator(func):
    def arithmetic(*args):
        print()
        return func(*args) / len(args)

    return arithmetic


@decorator
def calculations(*args):
    print('Сумма чисел : 2, 3, 3, 4 =', sum(args))
    return sum(args)


print('Среднее арифметическое : 2, 3, 3, 4 =', calculations(2, 3, 3, 4))