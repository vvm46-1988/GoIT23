# Логічні операції

class Car:
    store_name = 'GoIT store'

    def __init__(self, year, mark, model, color, price):
        self.year = year
        self.mark = mark
        self.model = model
        self.color = color
        self.price = price

    def __repr__(self):
        return f"Car('{self.color}', '{self.model}', '{self.mark}', {self.year})"

    def __str__(self):
        return f"{self.mark} {self.model}"

    def __eq__(self, other):
        return self.year == other.year

    def __ne__(self, other):
        return self.year != other.year

    def __lt__(self, other):
        return self.price < other.price

    def __gt__(self, other):
        return self.price > other.price

    def __le__(self, other):
        return self.price <= other.price

    def __ge__(self, other):
        return self.price >= other.price


    def __add__(self, other):
        return self.year + other.year


car_audi = Car(2023, 'Audi', 'A6', 'white', 19500)
car_bmw = Car(2022, 'BMW', 'X5', 'black', 19500)
print(car_audi == car_bmw)  # __eq__
print(car_audi != car_bmw)  # __ne__
print(car_audi < car_bmw)  # __lt__
print(car_audi > car_bmw)  # __gt__
print(car_audi <= car_bmw)  # __le__
print(car_audi >= car_bmw)  # __ge__
print(car_audi + car_bmw)
