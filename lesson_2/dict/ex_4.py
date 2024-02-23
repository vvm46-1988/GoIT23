# get
first = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
print(first['a'])
print(first['d'])
# print(first['f'])
print(first.get('a'))
print(first.get('f', 'Hello world'))
first['a'] = 'djhdjhdjhfdjhfdjfhdjfd'
print(first['a'])
print(list(first.keys()))
print(list(first.values()))
print(first.items())