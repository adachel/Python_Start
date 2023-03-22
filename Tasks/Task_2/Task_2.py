# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

print('Введите число: ')
number = int(input())
summa = 0
for i in range(1, number + 1):
    summa = summa + i
print('Сумма чисел до введенного числа: ', summa)    