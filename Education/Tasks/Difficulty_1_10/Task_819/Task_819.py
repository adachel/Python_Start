# Hеобходимо определить площадь поверхности и объем прямоугольного параллелепипеда. 
# INPUT.TXT содержит разделенные пробелом три натуральных числа a, b и c – измерения параллелепипеда. 
# OUTPUT.TXT выведите через пробел два целых числа: площадь поверхности и объем заданного параллелепипеда.

def Square(a, b, c):
    res = (a * b * 2) + (a * c * 2) + (c * b * 2)
    return res

def Volume(a, b, c):
    res = a * b * c
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_819\input.txt', 'r') as input_data:
    a, b, c = map(int, input_data.read().split())
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_819\output.txt', 'w', encoding= 'utf - 8') as output_data:
    output_data.write(f'Площадь и объем: {str(Square(a, b, c))} {str(Volume(a, b, c))}')

print(Square(a, b, c), Volume(a, b, c))
