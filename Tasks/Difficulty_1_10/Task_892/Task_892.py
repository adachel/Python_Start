# По заданному номеру месяца в году требуется определить время года.
# Входной файл INPUT.TXT содержит натуральное число N (N≤100) – номер месяца.
# В выходной файл OUTPUT.TXT выведите для летних месяцев значение «Summer», 
# для зимних – «Winter», для весенних – «Spring», для осенних – «Autumn». 
# Если число не соответствует возможному значению месяца, то в этом случае следует вывести «Error».

def Calc(n):
    if n > 0 and n <= 2 or n == 12:
        res = 'Winter'
    elif n > 2 and n <= 5:
        res = 'Spring'
    elif n > 5 and n <= 8:
        res = 'Summer'
    elif n > 8 and n <= 11:
        res = 'Autumn'
    else: res = 'Error'
    return res
    
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_892\input.txt', 'r') as input_data:
    n = int(input_data.read())
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_892\output.txt', 'w') as output_data:
    output_data.write(Calc(n))
print(Calc(n))
    