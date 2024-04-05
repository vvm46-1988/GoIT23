# Написати Contex Manager FileReader, який пише в лог timestamp коли файл був відкритий,
# timestamp, коли файл був закритий, ім'я файлу, і як довго файл був відкритий з точністю до секунд.

from datetime import datetime
from time import sleep

class FileReader:
    def __init__(self, filename):
        self.file = None
        self.opened = False
        self.filename = filename
        self.log = ''
        self.timestamp = None

    def __enter__(self):
        self.file = open(self.filename, 'r')
        self.opened = True
        self.timestamp = datetime.now().timestamp()
        msg = f'{self.timestamp:<20}|{self.filename:^15}| open \n'
        self.log += msg
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.opened:
            self.file.close()
            timestamp = datetime.now().timestamp()
            diff = timestamp - self.timestamp
            msg = f'{timestamp:<20}|{self.filename:^15}| closed {diff}s \n'
            self.log += msg
            self.opened = False


reader = FileReader('new_file.txt')
with reader as file:
    sleep(1)
    print(file.read())

with reader as file:
    sleep(2)
    print(file.read())

print(reader.log)