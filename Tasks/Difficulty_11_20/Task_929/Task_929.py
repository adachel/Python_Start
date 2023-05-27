# Hаписать программу, которая по количеству очков, набранных первым игроком после броска, 
# определяет наименьшее и наибольшее количество очков, 
# которые может получить второй игрок за этот бросок. 
# INPUT.TXT содержит одно натуральное число n — количество очков, которые получил первый игрок. 
# OUTPUT.TXT выведите два разделенных пробелом целых числа: 
# минимальное и максимальное количество очков соответственно, 
# которые мог набрать второй игрок при таком броске кубиков.

def Dif(n):
    if n == 0: res = 0
    elif n == 1: res = 6
    elif n == 2: res = 5
    elif n == 3: res = 4
    elif n == 4: res = 3
    elif n == 5: res = 2
    elif n == 6: res = 1
    return res

def Calc(n):
    maximum = n * 6
    if n >= 6:
        minimum = Dif(n % 6) + n // 6
    else: minimum = Dif(n)
    res = str(minimum) + ' ' + str(maximum)
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_929\input.txt') as input_data:
    n = int(input_data.read())
minim = min(list(Calc(n).split()))
maxim = max(list(Calc(n).split()))
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_929\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write(f'Минимальное: {minim}, Максимальное: {maxim}')
  
print(Calc(n))
