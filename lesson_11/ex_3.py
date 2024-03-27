# Власні винятки
class MyException(Exception):
    def __init__(self, value):
        self.value = value


def foo(n: int):
    if n < 0:
        raise MyException(f'Value is {n} and it < 0')
    else:
        return 100

print(foo(-5))


