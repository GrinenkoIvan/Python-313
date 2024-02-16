from math import pi


func_limit = [
    lambda x: print(f'Площадь окружности радиуса {x}: {x ** 2 * pi}'),
    lambda x, y: print(f'Площадь прямоугольника размером {x}*{y}: {x * y}'),
    lambda a, b, h: print(f'Площадь трапеции a={a}, b={b}, h={h}: {(a + b) * h/2}'),
]

func_limit[0](2)
func_limit[1](10, 13)
func_limit[2](7, 5, 3)
