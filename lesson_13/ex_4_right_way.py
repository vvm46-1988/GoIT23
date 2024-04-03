class Animal:
    def __init__(self, nickname, age, weight):
        self.__nickname = None
        self.__age = None
        self.__weight = None

        # Спрацюють сеттери
        self.nickname = nickname
        self.age = age
        self.weight = weight

    @property  # getter для nickname
    def nickname(self):
        return self.__nickname

    @nickname.setter  # setter для nickname
    def nickname(self, nickname):
        print("setter")
        if len(nickname) > 0:
            self.__nickname = nickname
        else:
            raise ValueError("Тваринка має мати ім'я")

    @property  # getter для age
    def age(self):
        return self.__age

    @age.setter  # setter для age
    def age(self, age):
        self.__age = age

    @property  # getter для weight
    def weight(self):
        return self.__weight

    @weight.setter  # setter для age
    def weight(self, weight):
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError("Тваринка повинна мати вагу")


class Turtle(Animal):
    def __init__(self, nickname, age, weight):
        super().__init__(nickname, age, weight)

    # @property
    # def age(self):
    #     return self.__age

    @Animal.age.setter
    def age(self, age):
        if age in list(range(0, 150)):
            Animal.age.fset(self, age)
        else:
            raise ValueError("Черепашки стільки не живуть")


turtle = Turtle('Tortilla', 149, 5)
print(turtle.nickname, turtle.age, turtle.weight)
