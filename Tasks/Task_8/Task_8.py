# Во входном файле INPUT.TXT записаны три натуральных числа A, B и C через пробел. Числа A и B ≤ 10^2, а C ≤ 10^6.
# В выходной файл нужно вывести YES в том случае, если A*B=C и вывести NO в противном случае.

input_data = open('D:\Works\IT\Python_Start\Tasks\Task_8\input.txt', 'r')
a, b, c = map(int, input_data.read().split())
if (a * b) == c: result = 'Yes'
else: result = 'No'
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_8\output.txt', 'w')
output_data.write(result)

# Превод из десятичной в двоичную систему
# a = 9
# res = ''
# while a > 0:
#     res = str(res) + str(a % 2)
#     a = a // 2
# print(res)

# Превод из двоичной в десятичную
# a = 1001
# a_str = str(a)
# data = list(a_str)
# res = 0; count = 0
# for i in data:
#     res = res + int(i) * (2 ** count)
#     count += 1
# print(res)







