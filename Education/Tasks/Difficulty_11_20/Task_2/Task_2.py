# Требуется посчитать сумму целых чисел, расположенных между числами 1 и N включительно.

# print('Введите число: ')
# number = int(input())
# summa = 0
# for i in range(1, number + 1):
#     summa = summa + i
# print('Сумма чисел до введенного числа: ', summa)    

# input_data = open('D:/Works/IT/Python_Start/Tasks/Task_2/input.txt', 'r') # Открываем файл
# number = int(input_data.read())
# summa = 0
# for i in range(1, number + 1):
#     summa += i
# output_data = open('D:/Works/IT/Python_Start/Tasks/Task_2/output.txt', 'w') # Открываем файл
# output_data.write(str(summa))
# print(summa)

def Factorial(x): # ф-ци факториала числа "х"
    summa = 0
    for i in range(1, x + 1):
        summa += i
    return summa
input_data = open('D:\Works\IT\Python_Start\Tasks\Task_2\input.txt', 'r')
number = int(input_data.read())
factorial = Factorial(number)
input_data.close()
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_2\output.txt', 'w')
output_data.write(str(factorial))
output_data.close()
print(factorial)




