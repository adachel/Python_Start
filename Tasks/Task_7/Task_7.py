# input_data = open('D:/Works/IT/Python_Start/Tasks/Task_7/input.txt', 'r')
# data = input_data.read().split()
# data_max = '0'
# for i in data:
#     if i > data_max:
#         data_max = i
# output_data = open('D:\Works\IT\Python_Start\Tasks\Task_7\output.txt', 'w')
# output_data.write(data_max)
# print(data_max)

input_data = open('D:/Works/IT/Python_Start/Tasks/Task_7/input.txt', 'r')
a, b, c = map(int, input_data.read().split()) # Вариант 
data = str(max(a, max(b, c)))
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_7\output.txt', 'w')
output_data.write(data)

print(data)


