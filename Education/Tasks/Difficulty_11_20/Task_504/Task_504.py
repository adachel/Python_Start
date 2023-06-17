# Cтояло три цветочка, слева направо: G – герань, C – крокус и V – фиалка. 
# Каждое утро Маша меняла местами стоящий справа цветок с центральным цветком. 
# А Таня каждый вечер меняла местами левый и центральный цветок. 
# Требуется определить порядок цветов ночью по прошествии K дней.
# INPUT.TXT содержится натуральное число K – число дней (K ≤ 1000).
# OUTPUT.TXT вывести три английских буквы: «G», «C» и «V», описывающие порядок по истечении K дней (слева направо).

def Calc(n):
    arr = ['G', 'C', 'V']
    for i in range(0, n):
        a = arr[:2]
        b = arr[2:]
        arr = b + a
    return arr
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_504\input.txt', 'r') as input_data:
    n = int(input_data.read())

res = ''.join(Calc(n)) # собираем список в строку    

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_504\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write('Результат: ' + res)

  
print(res)
    

