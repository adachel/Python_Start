# Задача №17. Дан список чисел. Определите, сколько в нем встречается различных чисел.

from random import randint
def Func(arr):
    data = set(arr)
    res = len(data)
    return res

# n = 10
# arr = [randint(-5, 5) for i in range(n)]
# print(arr)
# print(Func(arr))


# Задача №19. Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – положительное число.

def Calc(arr, k):
    for i in range(0, len(arr) - k):
        temp = arr.pop(len(arr) - 1)
        arr.insert(0, temp)
    print(arr)
    pass

# K = 2
# n = 5
# arr = [randint(1, 10) for i in range(n)]
# print(arr)
# Calc(arr, K)


# Задача №21. Напишите программу для печати всех уникальных значений в словаре.

def Unic(arr):
    data = []
    for i in arr:
        for key, value in i.items():
            data.append(value)
    res = set(data)        
    return res

# arr = [{"V" : "S001"}, {"V" : "S002"}, {"VI" : "S001"}, {"VI" : "S005"}, {"VII" : "S005"}, {"V":"S009"}, {"VIII":"S007"}]
# print(Unic(arr))


#Задача №23. Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, 
# больших предыдущего (элемента с предыдущим номером)

def Count(arr):
    counter = 0
    for i in range(len(arr)):
        if arr[i] > arr[i - 1]: counter += 1
    return counter

n = 10
arr = [randint(-10, 10) for i in range(n)]
print(arr)
print(Count(arr))


