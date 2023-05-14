# Найдите количество единиц в двоичной записи заданного числа.

def Bin(x):     # Перевод в двоичную рекурсивно.
    if x <= 1:
        return '1'
    else:
        res = str(x % 2) + str(Bin(x // 2))
    return res

def Count(x):   # Считает кол-во '1' в двоичном числе
    count = 0
    for i in x:
        if i == '1':
            count += 1
    return count
        
input_data = open('D:\Works\IT\Python_Start\Tasks\Task_22\input.txt', 'r')
num = int(input_data.read())
input_data.close()
num_str = list(Bin(num)) # Перевод двоичного числа в список
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_22\output.txt', 'w')
output_data.write('Result: ' + str(Count(num_str)))
output_data.close()

print(Count(num_str))        
