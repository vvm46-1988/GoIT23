# Сховище з паролем

class KeyStore:
    def __init__(self, name, password):
        self.__name = None
        self.__password = None
        self.__secret = None

        self.name = name
        self.password = password

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def password(self):
        return 'No way to get password'

    @password.setter
    def password(self, value):
        if self.__password is None:
            self.__password = value
        else:
            if self.is_valid():
                self.__password = value

    @property
    def secret(self):
        return self.__secret

    @secret.setter
    def secret(self, value):
        if self.is_valid():
            self.__secret = value

    def is_valid(self):
        p = input('Enter your password: ')
        if self.__password == p:
            print('OK')
            return True
        print("Wrong password")
        return False


k_store = KeyStore('John', '123456')
print('Read password: ', k_store.password)
print('Set new password')
k_store.password = '7890'
print('Set secret value')
k_store.secret = 'Hello'
print('Read secret: ', k_store.secret)
