# День программиста отмечается в 255-й день года (при этом 1 января считается нулевым днем). 
# Требуется написать программу, которая определит дату (месяц и число григорианского календаря), 
# на которую приходится День программиста в заданном году.
# В григорианском календаре високосным является: год, номер которого делится нацело на 400 
# и год, номер которого делится на 4, но не делится на 100.
# INPUT.TXT записано целое число от 1 до 9999 включительно, которое обозначает номер года нашей эры.
# В единственную строку выходного файла OUTPUT.TXT нужно вывести дату Дня программиста в формате DD/MM/YYYY, 
# где DD — число, MM — номер месяца (01 — январь, 02 — февраль, ..., 12 — декабрь), YYYY — год в десятичной записи.

def Calc(n):
    if n / 4 == int(n / 4):
        res = f'12/09/{n}'
    else: res = f'13/09/{n}'
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_550\input.txt') as input_data:
    n = int(input_data.read())
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_550\output.txt', 'w') as output_data:
    output_data.write(Calc(n))
    
    
print(Calc(n))


