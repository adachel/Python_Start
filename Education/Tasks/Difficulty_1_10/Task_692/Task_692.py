# Задано целое число N. Требуется определить, является ли оно бинарным. 
# Входной файл INPUT.TXT содержит единственное целое число N, не превосходящее 10000 по абсолютной величине. 
# В выходной файл OUTPUT.TXT выведите YES, если заданное число является бинарным, и NO в противном случае.
import math

def Calc(N):
    m = math.log(N, 2)
    if float(m).is_integer() == True: # проверяем, есть ли что-то после запятой
        res = 'YES' # Это если нет
    else: res = 'NO'
    return res
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_692\input.txt', 'r') as input_data:
    N = int(input_data.read())
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_692\output.txt', 'w', encoding= 'utf - 8') as output_data:
    output_data.write('Результат: ' + Calc(N))

print(N, Calc(N))