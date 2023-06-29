def Func(*args): # при *args можно добавлять несколько аргументов
    res = ''
    for i in args:
        res += i
    return res

print(Func('a', 'b', 'c'))

from math import * # импортирует все функции модуля 'math'

import random as rm # далее в программе 'math' указывается как 'm1'


# Фибоначи
def Fibo(n):
    if n in [1, 2]:   # если 'n' находится в списке 1, 2
        return 1
    return Fibo(n - 1) + Fibo(n - 2)

# n = 35
# list_1 = []
# for i in range(1, n):
#     list_1.append(Fibo(i))
# print(list_1)

# def Quik_Sort(arr):
#     if len(arr) <= 1: return arr
#     else:
#         pivot = arr[0]
#         less = [i for i in arr[1:] if i <= pivot]
#         greater = [i for i in arr[1:] if i > pivot]
#         return Quik_Sort(less) + [pivot] + Quik_Sort(greater)

# # n = 100
# # arr = []
# # for i in range(n):
# #     arr.append(rm.randint(0, 100))
# # print(arr)
# # print(Quik_Sort(arr))


def Merge_Sort(arr): # сортировка слиянием
    ccc = len(arr)
    if ccc > 1:
        mid = ccc // 2
        left = arr[:mid]
        rigth = arr[mid:]
        Merge_Sort(left) 
        Merge_Sort(rigth)
        i = j = k = 0
        a = len(left)
        b = len(rigth)
        while i < a and j < b:
            if left[i] < rigth[j]:
                arr[k] = left[i] 
                i += 1
            else: 
                arr[k] = rigth[j] 
                j += 1
            k += 1
        while i < a:
            arr[k] = left[i]
            i += 1
            k += 1
        while j < b:
            arr[k] = rigth[j]
            j += 1 
            k += 1

n = 3
arr = [7, 2, 5, 9]
# for i in range(n):
#     arr.append(rm.randint(0, 100))
print(arr)
Merge_Sort(arr)
print(arr)

    