# Пусть, например, заданы три числа: a1, a2, a3. Ваша задача – по заданным трем числам определить: 
# можно ли их переставить так, чтобы сумма первых двух равнялась третьему. 
# Первая строка входного файла INPUT.TXT содержит три целых числа через пробел: a1, a2, a3. 
# В выходной файл OUTPUT.TXT выведите слово «YES», если заданные числа можно переставить так, 
# чтобы сумма первых двух равнялась третьему. В противном случае выведите в выходной файл слово «NO».

def Calc(x, y, z):
    if x == (y + z) or y == (x + z) or z == (x + y):
        res = 'YES'
    else: res = 'NO'
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_970\input.txt', 'r') as input_data:
    a1, a2, a3 = map(int, input_data.read().split())
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_970\output.txt', 'w') as output_data:
    output_data.write(Calc(a1, a2, a3))
       
print(Calc(a1, a2, a3))