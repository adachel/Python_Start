# Отрезок задан координатами своих концевых точек. Требуется вычислить длину этого отрезка. 
# INPUT.TXT координаты концов отрезка X1 Y1 X2 Y2 . Все координаты – целые числа, не превышающие 1000. 
# OUTPUT.TXT выведите длину отрезка.

import math
def Calc(arr):
    x1 = arr[0]; y1 = arr[1]
    x2 = arr[2]; y2 = arr[3]
    res = int(math.sqrt(pow((x2 - x1), 2) + pow((y2 - y1), 2)))
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_529\input.txt', 'r') as input_data:
    arr = list(map(int, input_data.read().split()))
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_529\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write(f'Длина отрезка: {Calc(arr)}')
    
print(Calc(arr))