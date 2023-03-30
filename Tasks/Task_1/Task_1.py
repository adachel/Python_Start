# Требуется сложить два целых числа А и В. В единственной строке записаны два натуральных числа через пробел.
# Нужно вывести одно целое число — сумму чисел А и В

# print('Введите два числа через пробел')
# data = list(map(int, input().split()))
# A = data[0]
# B = data[1]
# summa = A + B
# print('Результат сложения: ', summa)

# input_data = open('D:/Works/IT/Python_Start/Tasks/Task_1/input.txt', 'r') # Открываем файл
# data = input_data.read().split(' ') # Принимаем и разбиваем данные по пробелу
# A = int(data[0])
# B = int(data[1])
# summa = str(A + B) # Переводим результат в string
# output_data = open('D:/Works/IT/Python_Start/Tasks/Task_1/output.txt', 'w') # Открываем файл
# output_data.write(summa) # Записывает только string
# print('Результат сложения: ', summa)

summa = lambda x, y: x + y # Создали lambda-фун-цию
input_data = open('D:\Works\IT\Python_Start\Tasks\Task_1\input.txt', 'r')
A, B = map(int, input_data.read().split()) # Присваиваем А и В значения из файла
res = summa(A, B) # res - присваиваем значение ф-ции summa
input_data.close()
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_1\output.txt', 'w')
output_data.write(str(res))
output_data.close()
print(res)





