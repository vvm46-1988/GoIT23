# Декоратори
# Шаблон проектування, який полягає в тому, щоб розширювати існуючий функціонал,
# не вносячи змін у код цього самого функціоналу.
"""
Напишіть decorator, який записує в консоль два повідомлення журналу:

: call [номер_виклику_функції]: [ім'я функції][її аргументи]\n
: result: [ім'я функції][результат]\n
"""
import sys
import functools

# decorator
def logger(func):
    call_count = 0

    @functools.wraps(func)
    def inner(*args, **kwargs):
        nonlocal call_count
        call_count += 1
        sys.stdout.write(f": call [{call_count}]: [{func.__name__}][{args}]\n")
        result = func(*args, **kwargs)
        sys.stdout.write(f": result: [{func.__name__}][{result}]\n")
        return result
    return inner


@logger
def mul(a, b):
    return a * b


@logger
def add(a, b):
    return a + b


print(mul(4, 8))
print(add(4, 5))
print(mul(6, 9))
print(mul(5, 9))
print(add(46, 5))
print(add.__name__)  # inner - wrong, add - correct
