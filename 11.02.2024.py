from math import sqrt


class Rectangle:
    def __init__(self, length, height):
        self.length = length
        self.height = height
        self.area = self.length * self.height
        self.perimeter = 2 * (self.length + self.height)
        self.diagonal = round(sqrt(self.length ** 2 + self.height ** 2), 2)

    def get_length(self):
        return f'Длина прямоугольника: {self.length}'

    def get_height(self):
        return f'Ширина прямоугольника: {self.height}'

    def get_area(self):
        return f'Площадь прямоугольника: {self.area}'

    def get_perimeter(self):
        return f'Периметр прямоугольника: {self.perimeter}'

    def get_diagonal(self):
        return f'Гипотенуза прямоугольника: {self.diagonal}'

    def __str__(self):
        graphic = ''
        for i in range(self.length):
            if i == 0 or i == self.length - 1:
                graphic += '* ' * self.height + '\n'
            else:
                graphic += '* ' + '  ' * (self.height - 2) + '*' + '\n'
        return graphic


rectangle = Rectangle(3, 9)
print(rectangle.get_length())
print(rectangle.get_height())
print(rectangle.get_area())
print(rectangle.get_perimeter())
print(rectangle.get_diagonal())
print(rectangle)