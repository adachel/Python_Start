# В первой строке входного файла INPUT.TXT записаны три натуральных числа через пробел. 
# Каждое из чисел не превышает 10^100. Числа записаны без ведущих нулей.
# В выходной файл OUTPUT.TXT нужно вывести одно целое число — максимальное.

# input_data = open('D:/Works/IT/Python_Start/Tasks/Task_7/input.txt', 'r')
# data = input_data.read().split()
# data_max = '0'
# for i in data:
#     if i > data_max:
#         data_max = i
# output_data = open('D:\Works\IT\Python_Start\Tasks\Task_7\output.txt', 'w')
# output_data.write(data_max)
# print(data_max)

# input_data = open('D:/Works/IT/Python_Start/Tasks/Task_7/input.txt', 'r')
# a, b, c = map(int, input_data.read().split()) # Вариант 
# data = str(max(a, max(b, c))) # Поиск максимального числа
# output_data = open('D:\Works\IT\Python_Start\Tasks\Task_7\output.txt', 'w')
# output_data.write(data)
# print(data)

input_data = open('D:/Works/IT/Python_Start/Tasks/Task_7/input.txt', 'r')
data = list(input_data.read().split())
data_max = max(data)
input_data.close()
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_7\output.txt', 'w')
output_data.write(data_max)
output_data.close()
print(data_max)


