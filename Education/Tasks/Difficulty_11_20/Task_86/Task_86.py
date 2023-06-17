# Головоломка про ферзей
# Hужно было расставить максимальное количество ферзей на доске 8х8 так, чтобы хотя бы одно поле оказалось небитым. 
# Эта задача легко решается для доски 3х3, т.к. понятно, что более двух ферзей расставить таким образом на ней невозможно.
# INPUT.TXT записано натуральное число N – размеры шахматной доски N×N.
# OUTPUT.TXT нужно вывести максимальное количество ферзей, которых можно расставить на шахматной доске N×N так, 
# чтобы одна клетка оставалась небитой.

def Calc(n):
    pole = n ** 2
    no_free = 7
    for i in range(3, n):
        no_free += 3
    res = pole - no_free    
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_86\input.txt') as input_data:
    n = int(input_data.read())
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_86\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write('Результат: ' + str(Calc(n)))
    
print(Calc(n))


