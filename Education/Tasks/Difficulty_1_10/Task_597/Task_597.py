# Поле имеет форму круга радиусом r1. Были обнаружены два следа, имевшие форму кругов. Один имел радиус r2, 
# второй - радиус r3. Сообщается, что они находились внутри поля и не пересекались, ни один из них не лежал внутри другого. 
# Возможно, касались друг друга и/или границы поля. Необходимо написать программу, которая будет проверять, 
# могли ли иметь место события, описанные в газете. 
# Первая строка входного файла INPUT.TXT содержит три положительных целых числа через пробел - r1, r2, r3. 
# В выходной файл OUTPUT.TXT выведите слово YES, если информация, может соответствовать правде, и слово NO - иначе.

def Calc(r1, r2, r3):
    d1 = r1 * 2; d2 = r2 * 2; d3 = r3 * 2
    if d1 >= (d2 + d3):
        res = 'YES'
    else: res = 'NO'
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_597\input.txt', 'r') as input_data:
    r1, r2, r3 = map(int, input_data.read().split())
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_597\output.txt', 'w') as output_data:
    output_data.write(Calc(r1, r2, r3))
       
print(Calc(r1, r2, r3))