# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, 
# разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d. Каждое число вводится с новой строки.

def Func_var1(start, step, finish):
    res = start
    for i in range(1, finish):
        res += step
    return res

def Func_var2(start, step, finish):
    # res = start + (finish - 1) * step
    res = start + (finish - 1) * step
    return res

# a = int(input('Первый элемет: '))
# b = int(input('Шаг: '))
# c = int(input('Кол-во элементов: '))
# print(Func_var1(a, b, c))
# print(Func_var2(a, b, c))


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint
def Calc(arr, *args):
    res = []
    for i in range(len(arr)):
        if arr[i] >= args[0] and arr[i] <= args[1]:
            res.append(i)
    print(res)
    pass

arr = [randint(-50, 50) for i in range(20)]
print(arr)
minimum = int(input('Начало диапазона: '))
maximum = int(input('Конец диапазана: '))
Calc(arr, minimum, maximum)