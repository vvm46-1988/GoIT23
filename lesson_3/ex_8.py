# Задача: Напишіть програму, яка перевіряє, чи є введене число паліндромом.
num = input('Please enter a number: ')
# is_poly = num == num[::-1]
# print(is_poly)
# print(num[::-1] == num)
is_palindrom = True
for item in range(len(num) // 2):
    if num[item] != num[-item - 1]:
        is_palindrom = False
        break
if is_palindrom:
    print(num, ' is a palindrome.')
else:
    print(num, ' is not a palindrome.')
