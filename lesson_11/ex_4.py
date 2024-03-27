# Інкапсуляція
# Реалізувати валідацію дужок та допустимих символів засобами ООП

# ValidationError: Unbalanced brackets: at 0, at 17, at 18
# }<div><p>{ test }}</p</div>
# ^                ^^


class ValidationError(Exception):
    def __init__(self, *args, idx=None):
        self.idx = idx


class StringValidator:

    def __init__(self):
        self._text = None
        self._opens = "([{<"
        self._closes = ")]}>"
        self._message = ''

    def _is_balanced(self):
        """
        Цей метод перевіряє рядок на збалансованість дужок. Використовується стек для відстеження відкриваючих
        та закриваючих дужок. Якщо виявляються помилки, генерується виняток ValidationError.
        """
        stack = []  # Створення порожнього стеку для відстеження дужок
        errors = []  # Порожній список для зберігання позицій незбалансованих дужок

        # Проходимо по кожному символу у тексті
        for symbol_position, symbol in enumerate(self._text):
            if symbol in self._opens:  # Якщо символ - це відкриваюча дужка
                stack.append((symbol_position, symbol))  # Додаємо позицію та сам символ у стек
            elif symbol in self._closes:  # Якщо символ - це закриваюча дужка
                position = self._closes.index(symbol)  # Знаходимо відповідну позицію закриваючої дужки у списку _closes
                if stack and self._opens[position] == stack[-1][
                    1]:  # Перевіряємо, чи відповідає відкриваюча дужка у стеку поточній закриваючій
                    stack.pop()  # Якщо так, видаляємо відкриваючу дужку зі стеку
                else:
                    errors.append(symbol_position)  # Інакше, додаємо позицію закриваючої дужки у список помилок

        # Після проходження всього тексту, перевіряємо, чи є помилки або чи залишилися незакриті дужки
        if errors or stack:
            errors.extend([s[0] for s in stack])  # Додаємо позиції незакритих дужок до списку помилок
            self._get_message('Unbalanced brackets', sorted(errors))  # Створюємо повідомлення про незбалансовані дужки
            raise ValidationError(self._message,
                                  idx=sorted(errors))  # Викидаємо виняток з позначенням помилкових позицій

    def _is_alphanumeric(self):
        """
        Цей метод перевіряє, чи містяться в рядку лише допустимі символи.
        Якщо виявляються неприпустимі символи, генерується виняток ValidationError.
        """
        pass

    def _get_message(self, base: str, error_details: list):
        """
        Цей метод формує повідомлення про помилку на основі базового повідомлення та деталей помилки.
        """
        # Створюємо рядок, який містить деталі помилки, де кожен елемент представляє позицію помилки
        res = ', '.join(f'at {error}' for error in error_details)

        # Формуємо повідомлення про помилку, додавши базовий текст та деталі помилки
        self._message = f"{base}: {res}"

    def _mark_errors(self, indexes):
        """
        Цей метод позначає місця в рядку, де виявлені помилки, знаком '^'.
        """
        # Створюємо список знаків '^' або пробілів для кожного символу у рядку
        marks = ['^' if i in indexes else ' ' for i in range(len(self._text))]

        # Повертаємо рядок з текстом та позначеннями помилок
        return f'{self._text}\n{"".join(marks)}'

    def validate(self, text):
        """
        Цей метод викликає два попередні методи для перевірки рядка.
        Якщо виявлено помилки, вони виводяться на екран, і генерується витяток.
        """
        self._text = text
        try:
            self._is_balanced()
            self._is_alphanumeric()
        except ValidationError as err:
            print(self._mark_errors(err.idx))
            raise err
        return True


if __name__ == '__main__':
    input_text = '}<div><p>{ test }</p</div>'
    validator = StringValidator()
    if validator.validate(input_text):
        print(input_text)
