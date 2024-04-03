# Методи __getitem__ i __setitem__
from collections import UserList


class PositiveNumber(UserList):
    def __init__(self, data=[]):
        super().__init__()
        self.data = [el for el in list(filter(lambda x: x > 0, data))]

    def __getitem__(self, index):
        if index:
            return self.data[index]
        return self.data

    def __setitem__(self, key, value):
        if value > 0 and key < len(self.data):
            self.data[key] = value

    def append(self, item):
        if item > 0:
            super().append(item)


nums = PositiveNumber([2, -4, 5, 8])
print(nums)
print(nums[None])
print(nums[1])
nums[100] = -6
print(nums)
nums.append(-7)
print(nums)
