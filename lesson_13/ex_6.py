"""
Розбираємо різницю між: звичайним методом, @classmethod и @staticmethod
"""


class Test:

    def doubler(self, x):  # self == test_obj
        print('Mul on 2')
        return x * 2

    @classmethod
    def triples(cls, x):  # cls == Test
        print(f'cls: {cls}')
        print('Mul on 3')
        return x * 3

    @staticmethod
    def quad(x):
        print('Mul on 4')
        return x * 4

test_obj = Test()
print('---Екземпляр класу---')
print(test_obj.doubler(4))
print(test_obj.triples(4))
print(test_obj.quad(4))
print('---Виклик через клас---')
# print(Test.doubler(4))  # Буде помилка
print(Test.triples(4))
print(Test.quad(4))
