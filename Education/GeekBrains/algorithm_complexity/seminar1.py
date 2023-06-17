# Задание 1. Сумма всех чисел от 1 до N.
# n = 16
# summa = 0
# counter = 0
# for i in range(1, n + 1):
#     summa += i
#     counter += 1
# print(summa, counter)
     
# Задание 2. Алгоритм поиска простых чисел     
# n = 20
# counter = 0
# for i in range(2, n):
#     for j in (2, i):
#         counter += 1
#         if i / j != int(i / j):
#             print(i)
# print(counter)
  
# Задание 3. алгоритм поиска всех доступных комбинаций (посчитать количество) для количества кубиков K с количеством граней N. 
# K = 4; N = 6
# counter = 0
# for i in range(N):
#     for j in range(N):
#         for k in range(N):
#             for l in range(N):
#                 for m in range(N):
#                     counter += 1
# print(counter)

# def Calc(k, n):
#     if k == 0: return 1
#     return Calc(k - 1, n) * n
# print(Calc(K, N))
      
# Задача 4. Алгоритм поиска нужного числа последовательности Фибоначчи.
n = 20; c = 1; arr = []
def Iter(n):
    a = [0,1]
    counter = 0
    for i in range(1, n):
        x = a[i] + a[i-1] 
        counter += 1
        a.append(x)
        res = a[-1]
    return res, counter

def Calc(n, c, arr):
    arr.append(c)
    print(sum(arr))
    if n == 1 or n == 2: return 1
    res = Calc(n - 1, c, arr) + Calc(n - 2, c, arr)
    return res

print(Calc(n, c, arr))
print(Iter(n))

