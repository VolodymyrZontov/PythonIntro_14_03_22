# параметры по умолчанию
# позиционные и именнованные аргументы
# типы переменных | аннотация типов
# импорт функций

############################################################################
import os
from utils.files import read_txt_file_as_str

path = "Homeworks"
list_dir = os.listdir(path)
print(list_dir)

filename = 'lesson_4_test.txt'
base_dir = ''
data = read_txt_file_as_str(f"{path}/{base_dir}/{filename}")
# data = read_txt_file_as_str(os.path.join(path, base_dir, filename))
print(data)
############################################################################
for filename in list_dir:
    filepath = os.path.join(path, filename)
    if os.path.isdir(filepath):
        print(filepath)
############################################################################
from utils.files import read_txt_file_as_str, DEBUG_MODE

data = read_txt_file_as_str('lesson_test.txt')
print(f"{__name__=}")
print(data)
print(DEBUG_MODE)

#######################################################################################
def get_args(*args, **kwargs):
    for arg_value in args:
        print(arg_value)
    for kwarg_value in kwargs:
        print(kwarg_value, kwargs[kwarg_value])


get_args(1, 2, 'qwe', name="John", age=12)
############################################################################
from random import choice, randint
from string import ascii_lowercase as alphabet

DEBUG_MODE = True


def create_email(domains, names, debug_mode=DEBUG_MODE):
    name = choice(names)
    number = randint(100, 999)
    some_str = "".join([choice(alphabet) for _ in range(randint(5, 7))])
    domain = choice(domains)
    e_mail = f"{name}.{number}@{some_str}.{domain}"
    if debug_mode:
        print(e_mail)
    return e_mail


names_list = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names=names_list)


def read_txt_file(filename="TEST.txt", debug_mode=DEBUG_MODE):
    with open(filename, 'r', encoding='utf-8') as my_file:
        data = my_file.read()
    if debug_mode:
        print(data)
    return data



data = read_txt_file('lesson_test.txt')
print(data)

data = read_txt_file()
