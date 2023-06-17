# Входной файл INPUT.TXT содержит одно натуральное число N - количество цветов бусин. 
# Требуется определить минимальное число бусин, которые можно не глядя вытащить из шкатулки так, 
# чтобы среди них гарантированно были две бусины одного цвета. 
# В выходной файл OUTPUT.TXT выведите ответ на поставленную задачу.

input_data = open('D:\Works\IT\Python_Start\Tasks\Task_903\input.txt', 'r')
n = int(input_data.read())
input_data.close()
res = n + 1
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_903\output.txt', 'w')
output_data.write('Result: ' + str(res))
output_data.close()

print(res)


