from collections import UserList
from random import randint


class MyList(UserList):
    _info = 'This is my list class'

    def get_positive(self):
        return list(filter(lambda x: x >= 0, self.data))

    def get_negative(self):
        return list(filter(lambda x: x < 0, self.data))

    def info(self):
        return self._info


r = []

for _ in range(0, 20):
    r.append(randint(-10, 10))
print(r)

result = MyList(r)
print(result)
print(result.get_positive())
print(result.get_negative())
print(result.info())
result.append(100000)
print(result.get_positive())
