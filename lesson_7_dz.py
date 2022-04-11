# 1. Дано целое число (int). Определить сколько нулей в этом числе.
number = 1200300400
number = str(number)
my_symbol = "0"
result = number.count(my_symbol)
print(result)

# 2. Дано целое число (int). Определить сколько нулей в конце этого числа.
# Например для числа 1002000 - три нуля
num = 1200300400
num = str(num)
result_num = len(num) - len(num.rstrip("0"))

# 3. Даны списки my_list_1 и my_list_2.
# Создать список my_result в который вначале поместить
# элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.

my_list_1 = ['q', 'w', 'e', 'r', 't', 'y']
my_list_2 = ["1", "2", "3", "4", "5"]

my_result = my_list_1[::2] + my_list_2[1::2]
print(my_result)

# 4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
# стоит на последнем месте в new_list. Если my_list [1,2,3,4], то new_list [2,3,4,1]

my_list = [1, 2, 3, 4]
new_list = my_list[:-1] + [my_list[0]]
print(new_list)

# 5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
# [1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)

my_list = ["POTATO", "TOMATO", "MEAT", "CHEESE"]
my_list.append(my_list.pop(0))
print(my_list)

# 6. Дана строка в которой есть числа (разделяются пробелами).
# Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
# Для данного примера ответ - 133. (используйте split и проверку isdigit)
test_str = "43 больше     чем 34 но меньше чем 56"

numb_list = []
for word in test_str.split():
    if word.isdigit():
        numb_list.append(int(word))
result = sum(numb_list)

# 7. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
# которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
# В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
# my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".

my_str = "My long string"
l_limit = "o"
r_limit = "g"
result = my_str[my_str.find(l_limit) + 1: my_str.rfind(r_limit)]
print(f"Substring: {result}")

# 8. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
# Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
# быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
# (используйте срезы длинны 2)
my_str = "qwert"
res_list = list()

temp = my_str + '_' if len(my_str) % 2 else my_str

for idx in range(0, len(temp), 2):
    res_list.append(temp[idx:idx + 2])

# 9. Дан список чисел. Определите, сколько в этом списке элементов,
# которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
# Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
# Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.

my_list = [2, 4, 1, 5, 3, 9, 0, 7]
result = 0

for index in range(1, len(my_list) - 1):
    if my_list[index] > my_list[index - 1] + my_list[index + 1]:
        result += 1

# 10. Дан список my_list в котором могут быть как строки (type str) так и целые числа (type int).
# Например [1, 2, 3, "11", "22", 33]
# Создать новый список в который поместить только строки из my_list.

my_list = [1, 2, 3, "11", "22", 33]
new_list = []
for value in my_list:
    if type(value) == str:
        new_list.append(value)
print(new_list)

# 11. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке ТОЛЬКО ОДИН раз.

my_str = "sssssssssssssssssssssssssssssssssssssssdfafafnkajshfkajsdfgjhgam,vc"
res_list = []
for symbol in set(my_str):
    if my_str.count(symbol) == 1:
        res_list.append(symbol)
print(res_list)

# 12. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.

my_str_1 = "akjsgfasc.kahscauzsckasc"
my_str_2 = "aksudhanmmsjskasla;a"
res_list = list(set(my_str_1).intersection(set(my_str_2)))
print(res_list)

# 13. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой ТОЛЬКО ПО ОДНОМУ разу.
# Пример: для строк "aaaasdf1" и "asdfff2" ответ ["s", "d"], т.к. эти символы есть в каждой строке по одному разу

my_str_1 = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaasdf1"
my_str_2 = "asdfff2"
res_list = []
for symbol in set(my_str_1).intersection(set(my_str_2)):
    if my_str_1.count(symbol) == 1 and my_str_2.count(symbol) == 1:
        res_list.append(symbol)
print(res_list)