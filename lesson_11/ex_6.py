"""
Базові принципи ООП - Наслідування

Наслідування є властивістю об'єктів породжувати своїх нащадків. Об'єкт-нащадок автоматично успадковує від батька все:
поля та методи, може доповнювати об'єкти новими полями та змінювати (перевизначати) методи батька або доповнювати їх.
"""


class Animal:
    def __init__(self, nickname: str, age: int) -> None:
        self.nickname = nickname
        self.age = age

    def get_info(self) -> str:
        return f"It's animal. His name is {self.nickname} and he's {self.age} years old"


class Cat(Animal):
    def __init__(self, nickname: str, age: int) -> None:
        super().__init__(nickname, age)

    def sound(self):
        return 'Meow'


cat = Cat('Vasya', 5)
print(cat.nickname)
print(cat.get_info())
print(cat.sound())
print(dir(cat))
