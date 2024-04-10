import csv

FILENAME = 'users.csv'

users = [
    {'name': 'Микола', 'age': 22, 'sex': 'male'},
    {'name': 'Марія', 'age': 25, 'sex': 'female'},
    {'name': 'Назар', 'age': 22, 'sex': 'male'},
]

with open(FILENAME, 'w', newline='', encoding='utf-8') as file:
    columns = ['name', 'age', 'sex']
    writer = csv.DictWriter(file, delimiter=';', fieldnames=columns)
    writer.writeheader()
    for user in users:
        writer.writerow(user)

with open(FILENAME, 'r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=';')
    for row in reader:
        print(row)
        print(type(row))
        print(row['name'], row['age'], row['sex'])
