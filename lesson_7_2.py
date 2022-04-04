# генераторы списков
# множества

my_str = "qwerty123"
my_list = []
for symbol in my_str:
    my_list.append(symbol)
my_list = [symbol for symbol in my_str]
print(my_list)

limit_value = 10
numbers = [number ** 0.5 for number in range(limit_value)]
print(numbers)

my_list = [12, 34, -54, 2, -6, 8]
result = [value ** 2 for value in my_list if value > 0]
print(result)

alphabet = [chr(index) for index in range(ord("a"), ord("z") + 1)]
print(alphabet)

#####################################################################
# множества

my_list = list('qwerty123ytrewq321')
my_set = set(my_list)  # нет повторов, не сохраняет порядок, изменяемый
print(my_set, type(my_set))


my_str = "bla BLA car"
result = len(set(my_str.lower()))
print(result)

my_list = [10, 2, 3, 2, 2, 3]
print(set(my_list))

my_set_1 = set("12345")
my_set_2 = {"1", "2", 3}

result_union = my_set_1.union(my_set_2)
print(result_union)

result_intersection = my_set_1.intersection(my_set_2)
print(result_intersection)

result_difference = my_set_2.difference(my_set_1)
print(result_difference)

my_str = "qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqa"
for symbol in set(my_str):
    print(symbol)