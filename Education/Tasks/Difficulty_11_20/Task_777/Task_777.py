# Лег спать в 10 часов вечера, завел будильник на 12 часов следующего дня. Проспать 14 часов не удалось
# будильник зазвонил через 2 часа. Исследователь забыл, что на будильнике, можно задать время менее 12 часов. 
# Напишите программу, которая определяет, сколько часов успеет проспать исследователь, прежде чем будильник его разбудит. 
# INPUT.TXT два целых числа S и T (1 ≤ S, T ≤ 12; S ≠ T), час, когда лег спать, и час, на который он установил будильник. 
# OUTPUT.TXT нужно вывести одно целое число – через сколько часов зазвонит будильник.

def Calk(arr):
    slip = arr[0]; alarm = arr[1]
    if alarm > slip:
        res = alarm - slip
    else: res = 12 - slip + alarm
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_777\input.txt', 'r') as input_data:
    arr = list(map(int, input_data.read().split()))
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_777\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write(f'Зазвонит через {Calk(arr)} часов')
    
    print(Calk(arr))
