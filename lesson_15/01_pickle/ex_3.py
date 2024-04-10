from pickle import loads, dumps

class A:
    x = 'some'
    def __init__(self):
        print('Hello world!')
        self.y = 'Another value'


a = A()
s = dumps(a)
s_class = dumps(A)

restored_a = loads(s)
restored_A = loads(s_class)

print(a.x, a.y)
print(restored_a.x, restored_a.y)
print(a == restored_a)  # False
print(A == restored_A)  # True