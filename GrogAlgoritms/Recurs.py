# СУММА ЭЛЕМЕНТОВ ЧЕРЕЗ РЕКУРСИЮ
# def sum_arr(arr, size):
#     if (size == 0):
#         return 0
#     else:
#         return arr[size - 1] + sum_arr(arr, size - 1)
# n = int(input("Введите длину списка:"))
# a = []
# for i in range(0, n):
#     element = int(input("Введите элемент списка:"))
#     a.append(element)
# print("Весь список:")
# print(a)
# print("Сумма элементов списка равна:")
# b = sum_arr(a, n)
# print(b) 

# КОЛ-ВО ЭЛЕМЕНТОВ В СПИСКЕ
# def F(a):
#      if a == []:
#          return 0
#      else:
#          return 1 + F(a[1:]) # Выводит с 1 до конца

# arr = [1, 2, 3, 7]
# print(F(arr))
# print(arr[0:])

# МОЙ КОД
# def FuncMax(arr, size, m): # МАКСИМАЛЬНОЕ ЧИСЛО В СПИСКЕ
#     if size < 0:
#         return m
#     elif arr[size] > m:
#         m = arr[size]
#     return FuncMax(arr, size - 1, m)

# def FuncSum(arr, size, summa): # СУММА ЭЛЕМЕНТОВ
#     if size < 0:
#         return summa
#     else:
#         summa += arr[size]
#     return FuncSum(arr, size - 1, summa)

# def FuncCalk(arr): # КОЛИЧЕСТВО ЭЛЕМЕНТОВ
#     if arr == []:
#         return 0
#     else:
#         return 1 + FuncCalk(arr[1:])

# arr = [5, 2, 8, 4, 45]
# size = len(arr) - 1
# m = 0
# s = 0
# print(f'Максимальное число:\t\t{FuncMax(arr, size, m)}') 
# print(f'Сумма элементов в списке:\t{FuncSum(arr, size, s)}')
# print(f'Количество элементов в списке:  {FuncCalk(arr)}')

def Func(arr): # Кол-во элементов
    if arr == []:
        return 0
    else:
        return 1 + Func(arr[1:])

def FuncSum(arr, size, summa): # Сумма элементов
    if size < 0:
        return summa
    else: summa += arr[size]
    return FuncSum(arr, size - 1, summa)  

def FuncMax(arr, size, maxElem): # Максимаальный элемент
    if size < 0:
        return maxElem
    elif arr[size] > maxElem:
        maxElem = arr[size]
    return FuncMax(arr, size - 1, maxElem) 

def FuncBin(arr, x, low, hight): # Бинарный поиск индекса искомого числа
    if (low + hight) / 2 == x:
        return arr.index(x)
    elif (low + hight) / 2 > x:
        hight = (low + hight) / 2
    elif (low + hight) / 2 < x:
        low = (low + hight) / 2
    return FuncBin(arr, x, low, hight)
             
arr = [2, 5, 7, 10, 14, 25, 28, 33, 61, 211]
size = len(arr) - 1
temp = 0
x = 28 # Искомое число
low = arr[0]; hight = arr[len(arr) - 1]
print(f'Кол - во элементов:    {Func(arr)}')
print(f'Сумма элементов:       {FuncSum(arr, size, temp)}')
print(f'Максимаальный элемент: {FuncMax(arr, size, temp)}')
print(f'Индекс искомого числа: {FuncBin(arr, x, low, hight)}')
    


