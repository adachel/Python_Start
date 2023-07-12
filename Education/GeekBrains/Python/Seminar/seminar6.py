# def gh(x,y,*args,**kwargs):
#     print(x,y)
#     print(args)
#     print(kwargs)
# gh(4,5,10,11,12,13,age = 10,name = "anna")


#      1 2 3 4 5
#n:    4 3 2 1 0
#res:  1 2 4 8 16
# def recr(n,res = 1):
#     if n == 0:
#         return res
#     return recr(n - 1, res * 2)#16
# n = 4
# print(recr(n))


# def recr(n):
#     k = input()
#     if n == 0:
#         return k
#     a = recr(n - 1) + k
#     print(a)
#     return a
# n = 4
# print(recr(4))

# Задача №39. Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, 
# в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит 
# число N - количество элементов в первом массиве, затем N чисел - элементы массива. 
# Затем число M - количество элементов во втором массиве. Затем элементы второго массива.

def DifS(arr1, arr2, res = []): # на семинаре
    for i in arr1:
        if i not in arr2: 
            res.append(i)
    return res

def DifMy(arr1, arr2, res = []): # самостоятельно
    for i in range(len(arr1)):
        temp = None
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                temp = None
                break
            else: temp = arr1[i]
        if temp is not None: 
            res.append((temp))
    return res

# from random import randint
# arr1 = [randint(1,10) for i in range(5)]
# arr2 = [randint(1,10) for i in range(5)]
# print(*DifMy(arr1, arr2))
# print(*DifS(arr1, arr2))


# Задача №41. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определит 
# количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. 
# Сначала вводится число N — количество элементов в массиве. Далее записаны N чисел — элементы массива. 
# Массив состоит из целых чисел.

def FSem(arr, counter = 0):
    for i in range(1,len(arr)-1):
        if arr[i - 1] < arr[i] > arr[i + 1]:
            counter += 1
    return counter

def FMy(arr, res = 0):
    for i in range(1, len(arr) - 1):
        if arr[i + 1] < arr[i] > arr[i - 1]:
            res +=1
    return res

# from random import randint
# arr = [randint(1,10) for i in range(10)]
# print(arr)
# print(FMy(arr))
# print(FSem(arr))


# Задача №43. Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу. 
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать. 
# Вводится список чисел. Все числа списка находятся на разных строках.

def ParSem(arr, res = 0):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                res += 1
    return res

def ParMy(arr, res = 0):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                res += 1
    return res

# from random import randint
# arr = [randint(1,10) for i in range(10)]
# print(arr)
# print(ParMy(arr))
# print(ParSem(arr))

# N = int(input('Введите N: '))
# print(N)
# li1 = [int(input('Введите число: ')) for _ in range(N)]
# print(*li1)


# Задача №45. Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n 
# (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. 
# По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. 
# Программа получает на вход одно натуральное число k, не превосходящее 10^5. Программа должна вывести 
# все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, 
# разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

def FSemin(n):
    lst = []
    for i in range(n):
        summa = 0
        for j in range(1, i // 2 + 1):
            if i % j == 0:
                summa += j
        lst.append([i, summa])
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i][0] == lst[j][1] and lst[i][1]==lst[j][0]:
                print(lst[i][0],lst[j][0])


def Sum_Num(n):
    lst = []
    if n == 1: summa = 1
    for i in range(1, n):
        if n % i == 0:
            lst.append(i)
            summa = sum(lst)
    return summa
        
def FFF(n, temp = [], arr = []):
    for i in range(2, n):
        temp.append(Sum_Num(i))
    for i in range(len(temp)):
        for j in range(i + 1, len(temp)):
            if temp[i] != temp[j]:
                if Sum_Num(temp[i]) == temp[j] and temp[i] == Sum_Num(temp[j]):
                    a = temp[i]; b = temp[j]
                    arr.append([a, b])         
    print(arr)

n = 1000
# print(Sum_Num(n))
FFF(n)
FSemin(n)

