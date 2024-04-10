# Створення системи управління користувачами для веб-сайту з
# можливістю додавання, перегляду та видалення користувачів.

import json

class UserManagementSystem:
    def __init__(self, database_file):
        self.database_file = database_file

    def load_users(self):
        try:
            with open(self.database_file, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def save_user(self, users):
        with open(self.database_file, 'w', encoding='utf-8') as file:
            json.dump(users, file)

    def add_user(self, user):
        users = self.load_users()
        # TODO: додавати користувача тільки тоді, коли такої id немає у файлі
        users.append(user)
        self.save_user(users)
        print('User was added')

    def view_users(self):
        users = self.load_users()
        if users:
            print('List of users:')
            for user in users:
                print(user)
        else:
            print('No users found')

    def delete_user(self, user_id):
        # TODO: clean list
        users = self.load_users()
        for user in users:
            if user['id'] == user_id:
                users.remove(user)
                print('User was deleted')
                self.save_user(users)
                return
        print('User with id {} not found'.format(user_id))

    def clean_file(self):
        pass


if __name__ == '__main__':
    user_management = UserManagementSystem('users.json')

    user_management.add_user({'id': 1, 'name': 'Ivan', 'email': 'ivan@gmail.com'})
    user_management.add_user({'id': 2, 'name': 'Petro', 'email': 'petro@gmail.com'})
    user_management.add_user({'id': 3, 'name': 'Hanna', 'email': 'hanna@gmail.com'})

    user_management.view_users()

    user_management.delete_user(1)