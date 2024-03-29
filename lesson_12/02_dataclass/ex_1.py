from dataclasses import dataclass
class ClassicClass:
    def __init__(self, attr_1, attr_2):
        self.attr_1 = attr_1
        self.attr_2 = attr_2

    def __eq__(self, other):
        return self.attr_1 == other.attr_1


obj_1 = ClassicClass(10, 'Hello')
obj_2 = ClassicClass(10, 'World')

print(obj_1 == obj_2)


@dataclass(init=True, eq=False, repr=False, order=False, unsafe_hash=False, frozen=True)
class DataClass:
    attr_1: int
    attr_2: str


data_obj_1 = DataClass(10, 'Hello')
data_obj_2 = DataClass(10, 'Hello')

print(data_obj_1 == data_obj_2)
