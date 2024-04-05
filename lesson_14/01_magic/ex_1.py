# Функтор - потрібний коли ми хочемо викликати екземпляр об'єкта як функцію
# Функтор - це коли екземпляр класу може сам себе викликати

class Count:
    def __init__(self, init_steps):
        self.steps = init_steps  # кроки

    def __call__(self, *args, **kwargs):
        inc, = args  # args -> tuple -> (25, )
        self.steps += inc


count_step = Count(100)  # Є якась людина, яка біжить і вона уже пробігла 100 кроків
count_step(25)  # пробіг ще 25 кроків
count_step(35)  # пробіг ще 35 кроків
print(count_step.steps)
