# 1) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str.
# Напечатать ЧИСЛО сколько раз my_symbol встречается в my_str.
# Пример:  my_str="blablacar", my_symbol="bla".
# Вывод на экран:
# 2

my_str = "blablacar"
my_symbol = "bla"

result = my_str.count(my_symbol)
print(result)

# 2) У вас есть переменная my_str, тип - str. И переменная my_symbol, тип - str.
# Напечатать столько раз my_symbol, сколько он встречается в my_str.
# Пример:  my_str="blablacar", my_symbol="bla".
# Вывод на экран:
# bla
# bla

count = my_str.count(my_symbol)
for _ in range(count):
    print(my_symbol)

# 3) У вас есть переменная my_str, тип - str. Напечатать ЧИСЛО сколько
# РАЗНЫХ символов встречается в my_str.
# Большая и маленькая буква считается как один символ.
# Пробелы, запятые и т.д. считаем тоже как символы.
# Пример:  my_str="bla BLA car".
# Вывод на экран:
# 6

my_str = "bla BLA car"
my_str = my_str.lower()
# box = []
box = ""
for symbol in my_str:
    if symbol not in box:
        # box.append(symbol)
        box += symbol
result = len(box)
print(result)

# 4) Дана строка my_str и пустой список my_list.
# Заполнить my_list символами из my_str,
# которые стоят на четных местах в строке (считаем с 0)

my_str = "zhjdsgfz,jhvzxnvkzxnj"
my_list = []
print(id(my_list))
# 1a
for index, symbol in enumerate(my_str):
    if not index % 2:
        my_list.append(symbol)
# 1b
for symbol in my_str[::2]:
    my_list.append(symbol)
# 2
my_list.extend(list(my_str[::2]))
# 3
my_list += list(my_str[::2])

print(my_list, id(my_list))


# 5) Дана строка my_str, список str_index целых чисел в диапазоне от
# 0 до длинны строки минус 1, пустой список my_list.
# Заполнить my_list символами из my_str, которые стоят на местах с
# индексами из str_index

my_str = "qwertyuiop"
str_index = [0, 9, 9, 1, 5]
my_list = []

for index in str_index:
    value = my_str[index]
    my_list.append(value)
    # my_list.append(my_str[index])
print(my_list)

my_number = 12345670007654321999000

# 6) Дано целое число (int). Определить сколько цифр в этом числе.

result = len(str(my_number))
print(result)

# 7) Дано целое число. Определить наибольшую цифру в этом числе.

my_number = "123456789ABCDEFaй"
result = max(str(my_number))
print(result)

# 8) Дано целое число. Составить число (int) с цифрами в обратном порядке.

result = int(str(my_number)[::-1])
print(result)
# 9) Дано целое число. Составить число с цифрами в порядке возрастания(убывания).

number_str = str(my_number)
sort_number_list = sorted(number_str, reverse=True)
sort_number_str = "".join(sort_number_list)
result = int(sort_number_str)
print(result)

result = int("".join(sorted(str(my_number), reverse=True)))
print(result)

# 10) Даны списки my_list_1 и my_list_2.
# Создать список my_result в который поместить элементы из my_list_1 и
# my_list_2 через один, начиная с my_list_1.
# a) кол-во эл-тов одинаковое
# б) кол-во эл-тов разное

my_list_1 = [1, 2, 3, 4]
my_list_2 = [10, 20]
my_result = []

list_len = min(len(my_list_1), len(my_list_2))
for index in range(list_len):
    value_1 = my_list_1[index]
    value_2 = my_list_2[index]
    my_result += [value_1, value_2]

my_result += my_list_1[list_len:]
my_result += my_list_2[list_len:]
print(my_result)
