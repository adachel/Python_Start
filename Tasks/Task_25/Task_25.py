# В данной задаче необходимо сравнить два целых числа. 
# Запишите в выходной файл один символ "<", если A < B, ">", если A > B и "=", если A=B.

def Calk(a, b):
    if a > b:
        c = '>'
    elif a == b:
        c = '='
    else: c = '<'
    return c

input_data = open('D:\Works\IT\Python_Start\Tasks\Task_25\input.txt', 'r')
a, b = map(int, input_data.read().split())
input_data.close()
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_25\output.txt', 'w')
output_data.write('Result: ' + f"'{Calk(a, b)}'")
output_data.close()

print(Calk(a, b))