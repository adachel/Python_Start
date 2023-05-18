# Во входном файле INPUT.TXT записаны три натуральных числа A, B и C через пробел. Числа A и B ≤ 10^2, а C ≤ 10^6.
# В выходной файл нужно вывести YES в том случае, если A*B=C и вывести NO в противном случае.

input_data = open('D:\Works\IT\Python_Start\Tasks\Task_8\input.txt', 'r')
a, b, c = map(int, input_data.read().split())
if (a * b) == c: result = 'Yes'
else: result = 'No'
input_data.close()
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_8\output.txt', 'w')
output_data.write(result)
output_data.close()
print(result)









