# Створити систему обліку складу товарів. Система повинна дозволяти:
# - Додавати нові товари на склад.
# - Видаляти товари зі складу.
# - Змінювати кількість товарів на складі.
# - Виводити список товарів на складі.

# Розв'язок:
# Для реалізації цієї задачі ми будемо використовувати наступні класи:
# - Product - клас, який представляє один товар на складі.
# - Storage - клас, який представляє весь склад.

# Клас Product має наступні атрибути:
# - title - назва товару.
# - code - код товару.
# - count - к-сть товару на складі.

# Клас Storage має наступні атрибути:
# - products - список всіх товарів на складі.

# Методи класу Product:
# - init(self, title, code, count) - конструктор класу.
# - get_title(self) - повертає назву товару.
# - get_code(self) - повертає код товару.
# - get_count(self) - повертає к-сть товару на складі.
# - set_count(self, count) - змінює к-сть товару на складі.

# Методи класу Storage:
# - init(self) - конструктор класу.
# - add_product(self, product) - додає товар на склад.
# - remove_product(self, product) - видаляє товар зі складу.
# - get_products(self) - повертає список всіх товарів на складі.
