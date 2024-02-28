# Потрібно визначити студентів з балом вище середнього
# Користувач вводить дані про кількість студентів, імена та бал для кожного.
# Програма повинна визначити середній бал і імена студентів, чий бал вище середнього.

students = {}
count = int(input('How many students: '))
sum = 0
for i in range(count):
    name = input('Please enter name: ')
    point = int(input('Please enter point: '))
    students[name] = point  # {'Anna': 5, 'Andrii': 4}
    sum += point  # sum = sum + point
avg = sum / count
print(f'The average point is: {avg}. Students with average point is: ')
print(students)
for student in students:
    value = students[student]
    if value > avg:
        print(student)
