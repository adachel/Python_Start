# Вывести одно целое число — разницу между максимальным и минимальным числом
input_data = open('D:\Works\IT\Python_Start\Tasks\Task_21\input.txt', 'r')
data = list(input_data.read().split())
input_data.close()
arr = [int(x) for x in data]
elem_min = min(arr)
elem_max = max(arr)
result = elem_max - elem_min
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_21\output.txt', 'w')
output_data.write('Result: ' + str(result))
output_data.close()
print(result)