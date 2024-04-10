import csv


with open('name.csv', 'w', newline='\n') as csv_file:
    fieldnames = ['first_name', 'last_name']

    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()

    writer.writerow({'first_name': 'John', 'last_name': 'Smith'})
    writer.writerow({'first_name': 'Tony', 'last_name': 'Stark'})
    writer.writerow({'first_name': 'Jeremy', 'last_name': 'White'})

with open('name.csv') as csv_file:
    print(csv_file.read())
