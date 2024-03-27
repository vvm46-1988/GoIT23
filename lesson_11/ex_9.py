class Car:
    brand = ['AUDI']

Car.brand = 'audi'


c_1 = Car()
c_2 = Car()
c_1.brand[0] = 'VW'
print(c_1.brand)
print(c_2.brand)