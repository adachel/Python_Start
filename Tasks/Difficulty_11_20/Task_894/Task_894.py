# Заданы площадь кольца и радиус внешней окружности. Требуется определить радиус внутренней окружности.
# INPUT.TXT содержит два положительных вещественных числа: S и R1 – площадь кольца и радиус внешней окружности соответственно. 
# Радиус внешней окружности не превышает 100.
# OUTPUT.TXT выведите радиус внутренней окружности R2 с точностью не худшей, чем 10^-3.

def Calc(arr):
    import math
    s = arr[0]; r1 = arr[1] # Площадь большого круга и большой радиус
    s_big = math.pi * r1 ** 2 # Площадь общего круга
    s_small = s_big - s # Порщадь малого круга
    r2 = round(math.sqrt(s_small / math.pi), 3)
    return r2

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_894\input.txt') as input_data:
    arr = list(map(float, input_data.read().split()))
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_894\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write(f'Результат: {Calc(arr)}')    

print(Calc(arr))   