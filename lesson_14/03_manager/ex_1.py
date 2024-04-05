"""
Для того, щоб об'єкт можна було використовувати в конструкції with... as...: в об'єкті повинні бути визначені два
методи: __enter__, __exit__.
__enter__ -- метод, який приймає лише один аргумент self. Якщо метод щось повертає, його результат буде
записаний у змінну val у конструкції with context_manager as val:.
__exit__ - обов'язково приймає 4 аргументи: self, exception type, exception value, exception traceback.
Ці аргументи необхідні коректної обробки винятків всередині __exit__.
"""


class FileWrite:
    def __init__(self, filename):
        self.file = None
        self.opened = False
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'w')
        self.opened = True
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.opened:
            self.file.close()
            self.opened = False


if __name__ == '__main__':
    with FileWrite('new_file.txt') as f:
        f.write('Hello world!\n')
        f.write('Happy end!\n')
