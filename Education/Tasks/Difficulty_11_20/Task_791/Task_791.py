# Клетки шахматной доски пронумерованы числами от 1 до 64 по строкам слева направо и снизу вверх. 
# Напишите программу, которая по заданному номеру клетки определяет номера всех клеток, имеющих с ней общую сторону.
# INPUT.TXT содержит одно целое число от 1 до 64.
# OUTPUT.TXT выведите через пробел в порядке возрастания номера всех клеток, имеющих с заданной общую сторону.

def Matrix():
    matrix = []
    for i in range(0, 64, 8):
        arr = []
        for j in range(1, 9):
            arr.append(j + i)
        matrix.append(arr)
    return matrix

def Calc(n):
    arr = Matrix()
    data = []
    for i in range(0, 8):
        for j in range(0, 8):
            if n == arr[i][j]:
                a = i; b = j           
    if n - 1 == arr[a][b - 1]: res_1 = arr[a][b - 1]
    else: res_1 = 0
    if n - 8 == arr[a - 1][b]: res_4 = arr[a - 1][b]
    else: res_4 = 0
    if a < 8 and b + 1 < 8:
        if n + 1 == arr[a][b + 1]: res_2 = arr[a][b + 1]
        else: res_2 = 0   
    else: res_2 = 0
    if a + 1 < 8 and b < 8:   
        if n + 8 == arr[a + 1][b]: res_3 = arr[a + 1][b]
        else: res_3 = 0    
    else: res_3 = 0
    data.append(res_1); data.append(res_2); data.append(res_3); data.append(res_4)
    for i in data:
        if i == 0: data.remove(0) 
    return data

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_791\input.txt') as input_data:
    n = int(input_data.read())
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_791\output.txt', 'w', encoding= 'utf-8') as output_data:
    for i in Calc(n):
        output_data.write(f'{i} ')

print(Calc(n))   