# Уравнениe вида A*X^3 + B*X^2 + C*X + D = 0. Bсе корни уравнений – целые числа и находятся на отрезке [-100, 100].
# В единственной строке входного файла INPUT.TXT записаны 4 числа: A, B, C и D – целые коэффициенты кубического уравнения. 
# Каждый коэффициент по модулю меньше 32768, A ≠ 0.
# В единственную строку выходного файла OUTPUT.TXT нужно вывести через пробел в порядке возрастания все корни 
# 3аданного кубического уравнения. Кратные корни следует выводить только один раз.

# input_data = open('D:\Works\IT\Python_Start\Tasks\Task_10\input.txt', 'r')
# A, B, C, D = map(int, input_data.read().split())
# res = ''
# for i in range(-100, 100):
#     if (A * i ** 3 + B * i ** 2 + C * i + D) == 0:
#         res = res + ' ' + str(i)
# output_data = open('D:\Works\IT\Python_Start\Tasks\Task_10\output.txt', 'w')
# output_data.write(res)   
# print(res)

def Calc(A, B, C, D):
    res = ''
    for i in range(-100, 100):
        if (A * i ** 3 + B * i ** 2 + C * i + D) == 0:
            res = res + ' ' + str(i)
    return res
input_data = open('D:\Works\IT\Python_Start\Tasks\Task_10\input.txt', 'r')
A, B, C, D = map(int, input_data.read().split())
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_10\output.txt', 'w')
output_data.write(Calc(A, B, C, D))
print(Calc(A, B, C, D))        
