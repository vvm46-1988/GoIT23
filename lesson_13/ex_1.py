# Методи __repr__ и __str__
class Car:
    store_name = 'GoIT23'

    def __init__(self, color, model, mark, year):
        self.color = color
        self.model = model
        self.mark = mark
        self.year = year

    def __repr__(self):
        return f"Car('{self.color}', '{self.model}', '{self.mark}', {self.year})"

    def __str__(self):
        return f"{self.mark} {self.model}"


car_obj = Car(color='black', model='Model', mark='Tesla', year=2023)
print(car_obj)  # print(str(car_obj))
print(repr(car_obj))


copy_obj = eval(repr(car_obj))  # TODO: Не робіть так!!!!
print(copy_obj.year)
print(copy_obj.model)
print(copy_obj.mark)
