# Известны результаты каждой из 4х четвертей баскетбольной встречи. 
# Нужно определить победителя матча. Побеждает команда, набравшая больше очков в течение всего матча. 
# Входной файл INPUT.TXT содержит 4 строки, в каждой строке находится два целых числа 
# a и b – итоговый счет в соответствующей четверти. а – количество набранных очков за четверть первой командой, 
# b – количество очков, набранных за четверть второй командой. 
# В выходной файл OUTPUT.TXT выведите номер выигравшей команды, в случае ничьей следует вывести «DRAW».

def Calk(arr):
    comp_one = 0
    comp_two = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if j % 2 == 0:
                comp_one += data[i][j]
            elif j % 2 == 1:
                comp_two += data[i][j]
    if comp_one > comp_two:
        res = 1
    elif comp_one < comp_two:
        res = 2
    else: res = 'DRAW'
    return res

data = []
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_61\input.txt', 'r') as input_data:
    for line in input_data:
        data.append([int(x) for x in line.split()])
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_61\output.txt', 'w', encoding= 'utf - 8') as output_data:
    output_data.write('Результат: ' + str(Calk(data)))

print(Calk(data))