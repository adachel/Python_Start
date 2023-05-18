# Маша и Миша собирали землянику. Машa X ягод, а Мишa – Y ягод. Bместе они съели Z ягод. 
# Входной файл INPUT.TXT натуральныe числа X, Y и Z, не превышающих 1000. 
# В выходной файл OUTPUT.TXT выведите количество собранных ягод, если наши подсчеты оказались правдоподобными, 
# либо слово «Impossible» в противном случае.

def Calc(X, Y, Z):
    if (X + Y) < Z:
        res = 'Impossible'
    else: res = (X + Y) - Z
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_755\input.txt', 'r') as input_data:
    X, Y, Z = map(int, input_data.read().split())
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_755\output.txt', 'w', encoding= 'utf - 8') as output_data:
    output_data.write('Результат: ' + str(Calc(X, Y, Z)))
     
print(Calc(X, Y, Z))

