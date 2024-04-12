# Реалізувати pickable клас, який зберігає дату та час коли об'єкт цього класу серіалізували та коли розпакували.
import pickle
from time import sleep
from datetime import datetime

class RememberAll:
    def __init__(self, *args):
        self.data = list(args)
        self.saved = None
        self.restored = None

    def __getstate__(self):
        state = self.__dict__.copy()
        state['saved'] = datetime.now()
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        self.restored = datetime.now()


r = RememberAll(1, 2, 3, 4, 5)

print(r.data)
r_dump = pickle.dumps(r)
sleep(1)
r_load = pickle.loads(r_dump)
print(r.saved, r.restored)
print(r_load.saved, r_load.restored)

# [1, 2, 3, 4, 5]
# None None
# None None