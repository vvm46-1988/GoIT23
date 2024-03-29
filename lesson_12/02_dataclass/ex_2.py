from dataclasses import dataclass

@dataclass(frozen=True)
class DataClass:
    attr_1: int = 0

a = DataClass()
a.attr_1 = 5
