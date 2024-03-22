# Замикання

def greeting(name):  # Зовнішня ф-ція

    def message(msg):  # Внутрішня ф-ція
        return f" {name} - {msg}"

    return message  # Повертаємо внутрішню ф-цію


msg_for_denys = greeting('Denys')  # msg_for_denys матиме доступ до name через замикання
msg_for_hanna = greeting('Welcome Hanna Mykhailivna')  # msg_for_denys матиме доступ до name через замикання

print(msg_for_denys('Go to lesson'))

a = msg_for_hanna("Go to rest")
b = msg_for_hanna("Go to shop")
c = msg_for_hanna("Go to work")
print(a)
print(b)
print(c)
