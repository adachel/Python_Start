# Входной файл INPUT.TXT содержит два целых числа: 
# K – коэффициент, отражающий во сколько раз Гулливер больше лилипутов, и M – количество слоев матрацев. 
# В выходной файл OUTPUT.TXT выведите количество матрацев лилипутов, необходимых для построения матраца для Гулливера.

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_773\input.txt', 'r') as input_data:
    K, M = map(int, input_data.read().split())
matr = K * K # Нужно еще и в ширь учитывать!
res = matr * M
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_773\output.txt', 'w', encoding= 'utf - 8') as output_data:
    output_data.write('Матрасов нужно Геркулесу: ' + str(res))
    
    
print(res)