class Cafe:
    def __init__(self):
        self.menu = {
            "кава": 25,
            "чай": 15,
            "какао": 30,
            "лате": 35
        }
        self.orders = []

    def __call__(self, item, quantity=1):
        if item in self.menu:
            total_price = self.menu[item] * quantity
            self.orders.append((item, quantity, total_price))
            print(f'Замовлено  {quantity} {item}. Загальна вартість: {total_price} грн.')
        else:
            print('Вибачте, такого напою немає!')

    def show_orders(self):
        if self.orders:
            print('Ваші замовлення:')
            for order in self.orders:
                print(f'{order[1]} * {order[0]} - {order[2]} грн.')
        else:
            print('У вас немає замовлень')


cafe = Cafe()

cafe('чай', 2)
cafe('лате', 1)
cafe('капучіно')
cafe.show_orders()


