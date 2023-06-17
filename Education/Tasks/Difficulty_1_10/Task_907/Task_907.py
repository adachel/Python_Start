# Удастся ли мышке спрятать круглый коврик под прямоугольным ковриком? 
# Первая строка входного файла INPUT.TXT содержит три натуральных числа через пробел: 
# W, H и R, где W и H - ширина и высота прямоугольного коврика, а R – радиус запасного коврика. 
# В выходной файл OUTPUT.TXT выведите «YES», если новый коврик можно спрятать под старым, 
# и слово «NO», если этого сделать нельзя.

def Calc(W, H, R):
    D = R * 2
    if D <= W and D <= H:
        res = 'YES'
    else: res = 'NO'
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_907\input.txt', 'r') as input_data:
    W, H, R = map(int, input_data.read().split())
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_907\output.txt', 'w') as output_data:
    output_data.write(Calc(W, H, R))
    
print(Calc(W, H, R))    