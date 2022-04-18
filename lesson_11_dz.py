# 8. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фамилию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
#
# Пример использования функции:
# names = ["king", "miller", "kean"]
# domains = ["net", "com", "ua"]
# e_mail = create_email(domains, names)
# print(e_mail)
# >>>miller.249@sgdyyur.com
from random import choice, randint
from string import ascii_lowercase as alphabet


def create_email(domains, names):
    name = choice(names)
    number = randint(100, 999)
    some_str = "".join([choice(alphabet) for _ in range(randint(5, 7))])
    domain = choice(domains)
    return f"{name}.{number}@{some_str}.{domain}"


def write_data(filename, data):
    pass


names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names)

write_data("test.txt", e_mail)

# names = ["qqqqqqqqq", "aaaaaaaa", "zzzzzzzzz"]
# domains = ["www", "ss", "uxxxa"]
# print(create_email(domains, names))
