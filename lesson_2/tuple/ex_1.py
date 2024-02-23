empty_tuple = ()
print(empty_tuple)
language = 'Python', 'C', "C#", 'Java', 'PHP'
print(language)
print(type(language))

p, c, *_ = language
print(p)
print(c)
print(_)
language[0] = 'Test'