# В строке входного файла INPUT.TXT записаны два натуральных числа K и N (1 ≤ K ≤ N ≤ 300). 
# К - максимальное количество ступенек, которое может преодолеть заяц одним прыжком, N – общее число ступенек лестницы.
# В строку выходного файла OUTPUT.TXT нужно вывести количество возможных вариантов различных маршрутов 
# на верхнюю ступеньку лестницы без ведущих нулей.

def Count(data, n, k):
    for i in range(1, n + 1):
        data.append(sum(data[max(0, i - k) : i]))
    return data

input_data = open('D:\Works\IT\Python_Start\Tasks\Task_11\input.txt', 'r')
n , k = map(int, input_data.read().split())
input_data.close()
data = [1]
Count(data, n, k)
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_11\output.txt', 'w')
output_data.write(str(data[n]))
print(Count(data, n, k))
print(data[n])
    

