# НОД
# Даны два натуральных числа A и B. Требуется найти их наибольший общий делитель (НОД).
# INPUT.TXT в единственной строке записаны натуральные числа A и B через пробел.
# OUTPUT.TXT выведите НОД чисел А и В.

def Calc(arr):
    arr_min = min(arr)
    for i in range(arr_min, 1, -1):
        if arr[0] % i == 0 and arr[1] % i == 0:
            res = i
            break
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_148\input.txt') as input_data:
    arr = list(map(int, input_data.read().split()))
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_148\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write('Результат: ' + str(Calc(arr)))
    
Calc(arr)    
