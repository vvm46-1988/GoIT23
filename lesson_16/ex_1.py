# __getstate__ i __setstate__
import pickle


class A:
    def __init__(self, important_data):
        self.important_data = important_data
        self.func = lambda: 7  # AttributeError: Can't pickle local object 'A.__init__.<locals>.<lambda>'
        self.is_valid = False  # Не хочу дану змінну серіалізувати

    def __getstate__(self):
        return [self.important_data]

    def __setstate__(self, state):
        self.important_data = state[0]
        self.func = lambda: 7
        self.is_valid = False


a = A('Hello world!')
s = pickle.dumps(a)

a_obj = pickle.loads(s)
print(a_obj.important_data)
# print(a_obj.func())
print(a_obj.is_valid)