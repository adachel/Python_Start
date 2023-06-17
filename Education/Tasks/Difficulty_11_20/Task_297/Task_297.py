# Ваша задача написать программу, которая определяет, сколько кругляшей в числе.
# INPUT.TXT записано целое число N.
# OUTPUT.TXT выведите одно число – количество кругляшей в числе N.

def Calc(n):
    arr = list(n)
    num = 0
    for i in arr:
        if i == '6' or i == '9' or i == '0': num += 1
        elif i == '8': num += 2
    res = num
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_297\input.txt') as input_data:
    n = (input_data.read())
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_297\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write(f'Кол-во "кругляшей": {Calc(n)}')
   
print(Calc(n))    
