# Задача №31. Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где a0 = 0, 
# a1 = 1, ak = ak-1 + ak-2 (k > 1). Требуется найти N-е число Фибоначчи

def Fibo(n):
    if n == 0: return 0
    if n == 1: return 1
    res = Fibo(n - 1) + Fibo(n - 2)
    return res


# n = int(input('Введите число: '))
# # n = 10
# print(Fibo(n))


# Задача №33. Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. 
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.

def Calc(arr):
    arr = list(map(int, arr.split()))
    maximum = minimum = arr[0]
    min_ind = max_ind = 0
    for i in range(len(arr)):
        if arr[i] < minimum: minimum = arr[i]; min_ind = i
        if arr[i] > maximum: maximum = arr[i]; max_ind = i
    arr[max_ind] = arr[min_ind]
    return arr

# arr = '1 3 7 3 4'
# print(Calc(arr))


# Задача №35. Напишите функцию, которая принимает одно число и проверяет, является ли оно простым. 
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число).

def Func(n):
    counter = 0
    for i in range(2, n - 1):
       if n % i == 0: counter += 1
    if counter > 0: res = 'No'
    else: res = 'Yes'
    return res

# n = 11
# print(Func(n))


# Задача №37. Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность 
# в обратном порядке. Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).

def Too1(n, arr, data = []):
    if n == 0: 
        data.append(arr[n])
        return data
    data.append(arr[n])
    return Too1(n - 1, arr)

def Too2(arr):
    data = arr[::-1]
    return data
    
arr = '3 4 5 6 7'
print(Too2(arr))
arr = arr.split()
n = len(arr)-1
print(*Too1(n, arr))
