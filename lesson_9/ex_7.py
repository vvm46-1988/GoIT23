# Валідація дужок
# ({[]}) - True
# ({[}}) - False

def is_balanced(input_string):
    opens = "([{"
    closes = ")]}"
    stack = []
    for symbol in input_string:
        if symbol in opens:
            stack.append(symbol)
        elif symbol in closes:
            position = closes.index(symbol)
            if stack and opens[position] == stack[-1]:
                stack.pop()
    if stack:
        return False
    else:
        return True

print(is_balanced('({[]})'))
print(is_balanced('({[}})'))
print(is_balanced('({[])'))
