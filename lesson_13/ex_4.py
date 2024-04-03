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
        if age in list(range(0, 50)):
            self.__age = age
        else:
            raise ValueError("Тваринки стільки не живуть")

    @property  # getter для weight
    def weight(self):
        return self.__weight

    @weight.setter  # setter для age
    def weight(self, weight):
        if weight > 0:
            self.__weight = weight
        else:
            raise ValueError("Тваринка повинна мати вагу")


dog = Animal('Rex', 2, 6)
print(dog.nickname)

# dog.nickname = ''
print(dog.nickname)
dog.age = 45
print(dog.age)
print(dog.weight)

