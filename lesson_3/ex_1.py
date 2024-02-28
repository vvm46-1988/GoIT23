# Скласти програму, яка на вхід отримує цілі числа k, l.
# Якщо вони не рівні, то менше з них замінюється більшим, інакше обидва замінюються на 0.

k = int(input("Enter a number k: "))
l = int(input("Enter a number l: "))

if k != l:  # True
    if k < l:
        k = l
    else:
        l = k
else:
    l = 0
    k = 0

print(k, l)
