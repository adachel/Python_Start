# В первой строке входного файла INPUT.TXT записано натуральное число N (1 ≤ N ≤ 1000) – количество дачников, 
# далее идут N строк, в каждой из которых описаны координаты каждого дачника и его участка:
# X Y X1 Y1 X2 Y2 X3 Y3 X4 Y4, (X, Y) – координаты приземления парашютиста. 
# (X1, Y1, X2, Y2, X3, Y3, X4, Y4) – координаты прямоугольного участка на плоскости, указанные последовательно.
# Все координаты – целые числа, не превышающие 50000 по абсолютной величине
# В выходной файл OUTPUT.TXT нужно вывести количество дачников, приземлившихся на свой участок. 
# Попадание на границу участка считается попаданием на участок.

from math import sqrt
L_otr = lambda x1, y1, x2, y2: sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2) # Расчет длины отрезка
def Geron(x, y, x1, y1, x2, y2):                                     # Формула Герона
    a = L_otr(x, y, x1, y1); b = L_otr(x1, y1, x2, y2); c = L_otr(x2, y2, x, y)
    p = (a + b + c) / 2
    S_ger = sqrt(p * (p - a) * (p - b) * (p - c))
    return S_ger

input_data = open('D:\Works\IT\Python_Start\Tasks\Task_12\input.txt', 'r')
N = int(input_data.readline())
temp = []
for i in range(1, N + 1):
    data = list(map(int, input_data.readline().split()))

    x = data[0]; y = data[1]   # Расчитываемая точка
    x1 = data[2]; y1 = data[3] # Точка А
    x2 = data[4]; y2 = data[5] # Точка В
    x3 = data[6]; y3 = data[7] # Точка С
    x4 = data[8]; y4 = data[9] # Точка D

    AB = L_otr(x1, y1, x2, y2); BC = L_otr(x2, y2, x3, y3)      

    S_arr = AB * BC # Площадь прямоугольника

    G1 = Geron(x, y, x1, y1, x2, y2); G2 = Geron(x, y, x2, y2, x3, y3)
    G3 = Geron(x, y, x3, y3, x4, y4); G4 = Geron(x, y, x4, y4, x1, y1)

    S_data = round((G1 + G2 + G3 + G4), 2) # Сумма площадей

    if S_arr == S_data: res = True
    else: res = False
    
    temp.append(res)
input_data.close()
result = str(sum(temp))
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_12\output.txt', 'w')
output_data.write(result)
output_data.close()
print(result)
    



