from dataclasses import dataclass


@dataclass
class Animal:
    name: str
    sound: str

    def make_sound(self):
        print(f'{self.name} makes sound')


@dataclass
class Cat(Animal):
    test: str

    def mouse(self):
        print(f'{self.name} is chasing a mouse')


my_cat = Cat(name='Bob', sound='Meow', test='Hello world')
my_cat.make_sound()
my_cat.mouse()
