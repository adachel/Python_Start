# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах. 
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

def InputSet(x):
    arr = set()
    [arr.add(int(input('Введите число: '))) for i in range(x)]
    print(arr)
    return arr

def Func(arr, data):
    res = sorted(list(arr & data))
    return res

# n = int(input('Введите кол-во элементов первого множества: '))
# arr = InputSet(n)
# m = int(input('Введите кол-во элементов второго множества: '))
# data = InputSet(m) 
# print(Func(arr, data))


# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
# причём кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. 
# всего на грядке растёт N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора 
# на них выросло различное число ягод — на i-ом кусте выросло a[i] ягод. В этом фермерском хозяйстве внедрена 
# система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста 
# и с двух соседних с ним. Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход 
# собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

from random import randint
def Var_1(arr):
    temp = 0
    arr_temp = []
    for i in range(0, len(arr)):
        if i == 0:
            temp = arr[-1] + arr[i] + arr[i + 1]
            arr_temp.append(temp)
        if i > 0 and i < len(arr) - 1:
            temp = arr[i - 1] + arr[i] + arr[i + 1]   
            arr_temp.append(temp)
        if i == len(arr) - 1:
            temp = arr[-1] + arr[-2] + arr[0]
            arr_temp.append(temp)
    res = max(arr_temp)
    return res

def Var_2(arr):
    arr_temp = []
    a = [arr_temp.append(arr[0] + arr[1] + arr[-1])]
    b = [arr_temp.append(arr[i - 1] + arr[i] + arr[i + 1]) for i in range(1, len(arr) - 1)]
    c = [arr_temp.append(arr[-1] + arr[-2] + arr[0])]
    res = max(arr_temp)
    return res

n = int(input('Введите кол-во кустов: '))
arr = [randint(1, 10) for i in range(n)]
print(arr)
print(f'Результат: {Var_1(arr)}')
print(f'Результат: {Var_2(arr)}')