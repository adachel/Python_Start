# Записано одно натуральное число А, оканчивающееся на цифру 5. 
# Для того, чтобы возвести число 125 в квадрат достаточно 12 умножить на 13 и приписать 25, 
# т.е. приписывая к числу 12*13=156 число 25, получаем результат 15625, т.е. 125^2=15625.
# Выведите одно натуральное число - A^2 без лидирующих нулей.

# print('Введите число, оканчивающееся на "5": ')
# number = int(input())
# if number > 5:
#     num_1 = number // 10
#     num_2 = num_1 + 1
#     summa = num_1 * num_2
#     result = str(summa) + '25'
# else:
#     result = 5 ** 2    
# print(result)

# input_data = open('D:/Works/IT/Python_Start/Tasks/Task_3/input.txt', 'r')
# number = int(input_data.read())
# if number > 5:
#     num_1 = number // 10
#     num_2 = num_1 + 1
#     summa = num_1 * num_2
#     result = str(summa) + '25'
# else:
#     result = 5 ** 2    
# output_data = open('D:/Works/IT/Python_Start/Tasks/Task_3/output.txt', 'w')
# output_data.write(str(result))
# print(result)

def Count(x):
    if x > 5:
        num1 = x // 10
        num2 = num1 + 1
        summa = str(num1 * num2) + '25'
    else: summa = str(5 ** 2)
    return summa
input_data = open('D:\Works\IT\Python_Start\Tasks\Task_3\input.txt', 'r')
number = int(input_data.read())
result = Count(number)
input_data.close()
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_3\output.txt', 'w')
output_data.write(result)
output_data.close()
print(result)




