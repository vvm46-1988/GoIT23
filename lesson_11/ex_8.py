"""
Базові принципи ООП - Поліморфізм

Поліморфізм - це властивість споріднених об'єктів (тобто об'єктів, що мають одного спільного батька)
вирішувати схожі за змістом проблеми різними способами.
"""


class Animal:
    def __init__(self, nickname: str, age: int):
        self.nickname = nickname
        self.age = age

    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return "Meow"


class Dog(Animal):
    def make_sound(self):
        return 5 * 155

animals = [Cat("Vasya", 4), Dog("Rex", 5)]

def animal_sounds(animals):
    for animal in animals:
        print(animal.make_sound())

animal_sounds(animals)

cat = Cat("Vasya", 4)
dog = Dog("Rex", 5)

print('-' * 10)
print(isinstance(dog, Animal))
print(isinstance(dog, Cat))
print(isinstance(dog, Dog))
print('-' * 10)
print(type(dog) is Animal)
print(type(dog) is Dog)