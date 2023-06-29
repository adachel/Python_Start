# n = 'rj\'ytk' # для вывода одной ковычки нужен обратный слэш
# z = 4
# x = 4.67
# print('{} - {} - {}'.format(n, z, x)) # вариант форматирования строки
# '''  тройные ковычки в начале и в конце закоментируют все нужные строки
# print(n)
# print(n)
# print(n)
# print(n)
# print(n)
# '''
# a = input('Введите число: ') # ввод с клавы
# print(a)

# a = 5.8
# b = 345.098
# print(round(a * b, 2))

n = int(input()) # Метод флажка, вместо 'break'
flag = True
i = 2
while flag:
    if n % i == 0:
        flag = False
        print(i)
    elif i > n // 2:
        print(n)
        flag = False
    i += 1


