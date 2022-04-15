# работа с файлами
# модуль os

filename = "Homeworks/lesson_4.txt"
# filename = "lesson_test.txt"
#####################################################################################
# так работать можно, если осторожно ))
my_file = open(filename, 'r')  # 'r', 'w', 'rb', 'wb',
data = my_file.read()
my_file.close()

#####################################################################################
# а так лучше
#####################################################################################
with open(filename, 'r') as my_file:
    data = my_file.read()

data = data.split("\n")
data.append("TEST TEXT \n")
data = "\n".join(data)

with open(filename.replace(".txt", "_test.txt"), 'w') as txt_file:
    txt_file.write(data)
#####################################################################################
with open(filename, 'r') as my_file:
    data = my_file.readlines()

data.append("TEST TEXT \n")

with open(filename.replace(".txt", "_test.txt"), 'w') as txt_file:
    txt_file.writelines(data)
