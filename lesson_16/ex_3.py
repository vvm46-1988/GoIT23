# Друк та нумерація рядків у текстовому файлі.
# 1: Думи мої, думи мої,
# 2: Лихо мені з вами!
# Серіалізую обєкт
# Десеріалізую і продовжую нумерацію і читання з файлу на тому місці де він був серіалізований

import pickle


class TextReader:
    def __init__(self, filename):
        self.filename = filename
        self.file = open(self.filename, encoding='utf-8')
        self.line_count = 0

    def readline(self):
        self.line_count += 1
        line = self.file.readline()
        if not line:
            return None
        if line.endswith('\n'):
            line = line[:-1]  # позбуваємось '\n'
        return f'{self.line_count}: {line}'
        # return '%i: %s' % (self.line_count, line)

    def __getstate__(self):
        hello_world = self.__dict__.copy()
        del hello_world['file']
        return hello_world

    def __setstate__(self, hello_world):
        print(hello_world)
        self.__dict__.update(hello_world)

        file = open(self.filename, encoding='utf-8')
        for _ in range(self.line_count):
            file.readline()
        self.file = file


reader = TextReader('poem.txt')
print(reader.readline())
print(reader.readline())
print(reader.readline())
print(reader.readline())
print(reader.readline())
print(reader.readline())

new_reader = pickle.loads(pickle.dumps(reader))  # повинен запамятати коли він був упакований і продовжити друкувати результат з того самого місця
while True:
    line = new_reader.readline()
    if line is None:
        break
    else:
        print(line)
print('-' * 10)
print(reader.readline())
print(reader.readline())