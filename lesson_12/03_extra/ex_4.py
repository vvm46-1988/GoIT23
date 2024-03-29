"""
Агрегація
Це коли екземпляр господаря створюється десь в іншому місці коду,
і передається в конструктор вихованця як параметр
"""


class Animal:
    def __init__(self, nickname, age):
        self.nickname = nickname
        self.age = age

    def info(self):
        return f"It's animal with name: {self.nickname}, age: {self.age}"


class Owner:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def info(self):
        return f"It's owner with name: {self.name}"


class Cat(Animal):
    def __init__(self, nickname, age, owner: Owner):
        super().__init__(nickname, age)
        self.owner = owner

    def sound(self):
        return 'SOUND'


owner = Owner('Vova', '0951111111')
print(owner.name)
print(owner.phone)
print(owner.info())

cat = Cat('Bob', 4, owner)
print(cat.owner.info())
print(cat.owner.name)
print(cat.owner.phone)