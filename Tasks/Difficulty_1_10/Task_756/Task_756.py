# Сеть прямоугольная размером M×N узлов. Разрыв это единичный обрыв лески между двумя смежными узлами сети. 
# INPUT.TXT содержит два целых числа M и N через пробел – размеры рыболовной сети. 
# OUTPUT.TXT выведите максимальное число разрывов заданной сети, которые не приведут к распадению рыболовной снасти.

import math

def Base(b): # базовый вариант, когда а = 2, а b - любое
    count = 0
    for i in range(2, b + 1):
        count += 1
    return count

def Odd(a): # когда a - нечетное
    count = 0
    for i in range(1, a + 1, 2):
        count = count + Base(b)
    res = count 
    return res

def Even(b): # добавка когда а - четное
    count = 0
    for i in range(0, b):
        count += 1
    res = math.ceil(count / 2) # округление в большую сторону. round работаает не корректно
    return res

def Comp(a, b): # сравнение выриантов
    if a == 2:
        res = Base(b) # только для а = 2
    if a % 2 == 1:
        res = Odd(a) # для нечетного "а"
    if a % 2 == 0 and a > 2:
        res = Odd(a) + Even(b) # для нечетного "а" + добавка
    return res
    
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_756\input.txt', 'r') as input_data:
    arr = list(map(int, input_data.read().split()))
    arr_sort = sorted(arr) # сортируем, чтобы меньшее число было - а, так получается наибольшее кол-во
    a = arr_sort[0]; b = arr_sort[1]
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_756\output.txt', 'w', encoding= 'utf - 8') as output_data:
    output_data.write('Результат: ' + str(Comp(a, b)))

print(f'Result: {Comp(a, b)}')


# Поэтому искомое количество разрывов должно быть равно разнице последних величин: 
# R2-R1 = N*(M-1) + M*(N-1) – (M*N-1) = (N-1)*(M-1), что и требовалось доказать.

print((a - 1) * (b - 1))

