# В единственной строке входного файла INPUT.TXT записано натуральное число от 1 до 100.
# В выходной файл OUTPUT.TXT нужно вывести в точности то же число, которое задано во входном файле.
input_data = open('D:\Works\IT\Python_Start\Tasks\Task_108\input.txt', 'r')
f = input_data.read()
input_data.close()
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_108\output.txt', 'w')
output_data.write('Result: ' + f)

print(f)