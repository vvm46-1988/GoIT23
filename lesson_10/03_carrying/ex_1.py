# Каррінг - це перетворення функції від багатьох аргументів на набір функцій,
# кожна з яких є функцією від одного аргументу.

# В нас є функція, яка приймає 2 параметра name, msg і за допомогою карринга ми розбиваємо її на декілька
# ф-цій з одним параметром

def greeting_simple(name, msg):
    return f"{name} - {msg}"


b = greeting_simple("Hanna", 'Hello')
print(b)


def greeting(name):
    def simple(msg):
        def third(text):
            def fourth(arg):
                return f"{name} - {msg}: Text is: {text}, arg: {arg}"
            return fourth
        return third
    return simple


greet = greeting('Hanna')
msg = greet('Hello')
text = msg('World')
arg = text(5)
print(arg)
