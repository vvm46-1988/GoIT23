"""
Асоціація
Це коли один клас включає інший клас як один з полів. Асоціація описується словом "має".
Тварина має господаря.

Виділяють два окремі випадки асоціації: композицію та агрегацію.

Композиція
Це коли господар не існує окремо від вихованця.
Він створюється при створенні вихованця і повністю управляється вихованцем.
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
    def __init__(self, nickname, age, name, phone):
        super().__init__(nickname, age)
        self.owner = Owner(name, phone)  # Композиція

    def sound(self):
        return 'SOUND'


cat = Cat('Bob', 4, 'Vova', '123-456-7890')
print(cat.owner.info())
print(cat.owner.name)
print(cat.owner.phone)