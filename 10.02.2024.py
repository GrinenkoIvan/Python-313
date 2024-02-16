class Auto():

    def __init__(self, model, year, manufacturer, engine_power, color, price):
        self.model = model
        self.year = year
        self.manufacturer = manufacturer
        self.engine_power = engine_power
        self.color = color
        self.price = price

    def print_auto(self):
        print(" Персональные данные ".center(40, "*"))
        print(f"\nНазвание модели: {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.manufacturer}\n"
              f"Мощность двигателя: {self.engine_power} л.с.\nЦвет машины: {self.color}\nЦена: {self.price}\n")
        print("=" * 40)

    def set_model(self, model):
        self.model = model

    def get_model(self):
        return self.model

    def set_year(self, year):
        self.year = year

    def get_year_of_issue(self):
        return self.year

    def set_manufacturer(self, manufacturer):
        self.manufacturer = manufacturer

    def get_manufacturer(self):
        return self.manufacturer

    def set_engine_power(self, engine_power):
        self.engine_power = engine_power

    def get_engine_power(self):
        return self.engine_power

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color

    def set_price(self, price):
        self.price = price

    def get_price(self):
        return self.price


my_car = Auto("model='X7 M50i'", "year='2021'", "manufacturer='BMW'", "engine_power=530", "color='white'",
              "price=10790000")

print(my_car.print_auto())
