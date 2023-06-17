# Напишите программу, которая выводит элемент из строки Y и столбца X матрицы размера N×M, которая заполнена следующим образом:
# INPUT.TXT содержит натуральные числа N, M, Y, X. N - количество строк матрицы, M - количество столбцов матрицы, 
# Y и X - номера строки и столбца искомого элемента. 
# OUTPUT.TXT выведите искомый элемент.

def Matrix(arr):
    n = arr[0]; m = arr[1]
    matrix = []
    for j in range(n):
        if j == 0:
            data = [i + j for i in range(m)]
            a = data[-1] + m
        elif j % 2 == 1:
            data = [a - i for i in range(m)]
            b = data[0] + 1
        elif j % 2 == 0 and j > 1:
            data = [i + b for i in range(m)]
            a = data[-1] + m
        matrix.append(data)
    return matrix

def Print_Matrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end= '\t')
        print()
    
def Calc(arr):
    x = arr[2]; y = arr[3]
    res = Matrix(arr)[x - 1][y - 1]
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_943\input.txt') as input_data:
    arr = list(map(int, input_data.read().split()))
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_943\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write('Результат: ' + str(Calc(arr)))    

print(Calc(arr))
    
    