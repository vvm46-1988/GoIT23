# Реалізувати клас, який буде на вхід приймати якесь число (суму коштів),
# і буде повертати скільки монет може входити в цю суму.
# In: 185
# Out: {50: 3, 25: 1, 10: 1, 5: 0, 2: 0, 1: 0}

class Coins:
    def __init__(self, total_sum):  # Констуктор
        self.coins = (1, 2, 5, 10, 25, 50)  # Антрибут екзепмпляра, він не змінюється
        self.total_sum = total_sum  # Антрибут екзепмпляра, значення передається під час створення екземпляра

    def change(self):  # Метод класу
        result = dict()
        item = len(self.coins) - 1
        while item >= 0:
            coin = self.coins[item]
            num_of_coin = self.total_sum // coin
            result[coin] = num_of_coin
            self.total_sum -= coin * num_of_coin
            item -= 1
        return result


ins = Coins(185)  # Створюємо екземпляри (Instance) класу
print(ins.coins)
print(ins.change())

ins_2 = Coins(174)
print(ins_2.change())
