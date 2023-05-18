# За задачу начисляется штраф в размере количества минут от начала соревнования до её посылки на проверку. 
# Если же и количество штрафного времени совпадает – то студент со старшего курса уступает победу студенту с младшего курса. 
# Первая строка входного файла INPUT.TXT содержит натуральное число N (N ≤ 10) – количество задач. 
# Во второй строке записаны через пробел N натуральных чисел – количество минут, необходимое для решения каждой задачи. 
# Время решения задачи не превосходит 300 минут. 
# В выходной файл OUTPUT.TXT выведите номер курса студента, одержавшего победу в олимпиаде.

def Calk(arr):
    summma = 0
    temp = 0
    for i in range(0, len(arr)):
        temp = temp + arr[i]
        summma = summma + temp
    return summma

with open('D:\Works\IT\Python_Start\Tasks\Task_942\input.txt', 'r') as input_data:
    arr = input_data.readlines()
n = int(arr[0]) # Число задач
five = list(map(int, arr[1].split())) # Алгоритм пятикурсника
three = five[::-1] # Алгоритм третекурсника
one = sorted(five) # Алгоритм первокурсника

if Calk(five) < Calk(three) and Calk(five) < Calk(one):
    result = '5'
elif Calk(three) <= Calk(five) and Calk(three) < Calk(one):
    result = '3'
else: result = '1'

with open('D:\Works\IT\Python_Start\Tasks\Task_942\output.txt', 'w') as output_data:
    output_data.write('Result: ' + result)
    
print(result)
