# По целочисленным координатам вершин треугольника требуется вычислить его площадь.
# INPUT.TXT содержит 6 целых чисел x1,y1,x2,y2,x3,y3 – координаты вершин треугольника. 
# OUTPUT.TXT выведите точное значение площади заданного треугольника. 
# Ф-ла Герона: p = (a + b + c) / 2; s = SQR(p * (p - a) * (p - b) * (p - c)). 
# Расстояние между точками: a = sqr((x2 - x1)^2 + (y2 - y2)^2)

def Calc(arr):
    import math
    a = math.sqrt(pow((arr[2] - arr[0]), 2) + pow((arr[3] - arr[1]), 2))
    b = math.sqrt(pow((arr[4] - arr[2]), 2) + pow((arr[5] - arr[3]), 2))
    c = math.sqrt(pow((arr[4] - arr[0]), 2) + pow((arr[5] - arr[1]), 2))
    p = (a + b + c) / 2
    s = round((math.sqrt(p * (p - a) * (p - b) * (p - c))), 1)
    return s

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_822\input.txt') as input_data:
    arr = list(map(int, input_data.read().split()))
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_822\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write('Площадь треугольника: ' + str(Calc(arr)))


