# Даны длины трех отрезков. Требуется проверить: могут ли они являться сторонами невырожденного треугольника.
# INPUT.TXT содержит три числа X Y Z – длины заданных отрезков. Длины отрезков не превышают 1000. 
# OUTPUT.TXT выведите YES, если отрезки могут быть сторонами треугольника и NO в противном случае.

def Calc(arr):
    X = arr[0]; Y = arr[1]; Z = arr[2]
    if X + Y > Z and Y + Z > X and X + Z > Y:
        res = 'Yes'
    else: res = 'No'
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_606\input.txt', 'r') as input_data:
    arr = list(map(int, input_data.read().split()))
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_606\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write('Результат: '+ Calc(arr))

print(Calc(arr))
    
