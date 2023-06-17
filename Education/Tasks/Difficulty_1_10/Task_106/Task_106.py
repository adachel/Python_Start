# Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной. 
# В первой строке входного файла INPUT.TXT записано натуральное число N (1 ≤ N ≤ 100) – число монеток. 
# В каждой из последующих N строк содержится одно целое число – 1 если монетка лежит решкой вверх и 0 если вверх гербом. 
# В выходной файл OUTPUT.TXT выведите минимальное количество монет, которые нужно перевернуть.

def Calc(arr):
    count_0 = 0
    count_1 = 0
    for i in range(1, len(arr)):
        if arr[i] == 0:
            count_0 += 1
        else: count_1 += 1
    if count_0 > count_1:
        res = f'Нужно перевернуть c "Решкой" {count_1} монет'
    else: res = f'Нужно перевернуть c "Орлом" {count_0} монет' 
    return res
        
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_106\input.txt', 'r') as input_data:
    arr = list(map(int, input_data.readlines()))
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_106\output.txt', 'w', encoding= 'utf - 8') as output_data:
    output_data.write(Calc(arr))
    
print(arr) 
print(Calc(arr))   