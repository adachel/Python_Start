# В строке входного файла INPUT.TXT записано число N (0 ≤ N ≤ 100). 
# В следующих N строках записано по N чисел, каждое из которых является единичкой или ноликом. 
# Причем, если в позиции (i, j) квадратной матрицы стоит единичка, то i-ый и j-ый города соединены дорогами, 
# а если нолик, то не соединены. Гарантируется, что все дороги соединяют различные города.
# В выходной файл OUTPUT.TXT необходимо вывести число, определяющее количество дорог на планете «Snowflake».

def Calk(data, n):
    count = 0
    for i in range(0, n):
        for j in range(0, i):
            if data[i][j] == data[j][i] and data[i][j] == 1:
                count +=1 
    return count    
       
input_data = open('D:\Works\IT\Python_Start\Tasks\Task_15\input.txt', 'r')
N = int(input_data.readline())
A = input_data.readlines()
Arr = [[int(n) for n in x.split()] for x in A] # читает из файла и создает список списков int
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_15\output.txt', 'w')
output_data.write(str(Calk(Arr, N)))
print(Calk(Arr, N))
         


    