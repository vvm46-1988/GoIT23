from collections import UserString

template = [
    "Ви можете досягти всього. Варто лише трохи постаратися і запастися книгами.",
    "Цей смартфон - справжня знахідка. Великий і яскравий екран, потужний процесор - все це в невеликому гаджеті.",
    "Зібрати камені нескінченності легко, якщо ви природжений герой.",
    "Освоїти верстку нескладно. Візьміть книгу нову книгу і закріпіть усі вправи на практиці.",
    "Боротися з прокрастинацією нескладно. Просто дійте. Маленькими кроками.",
    "Програмувати не настільки складно, як про це говорять.",
    "Прості щоденні вправи допоможуть досягти успіху."
]

# for i, comment in enumerate(template):
#     print("|{:^5}|{:<15}|".format(i, comment))


class Comments(UserString):
    def get_limit_comment(self, limit=10):
        return f"{self.data[:limit - 3]}..."


comments = [Comments(comment) for comment in template]

for i, comment in enumerate(comments):
    print("|{:^5}|{:<15}|".format(i + 1, comment.get_limit_comment(55)))
