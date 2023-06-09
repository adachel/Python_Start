# НАПЕРСТКИ
# Под первый (левый) он кладет маленький шарик. Затем он очень быстро выполняет ряд перемещений наперстков, 
# каждое из которых – это одно из трех перемещений - A, B, C:
# A - обменять местами левый и центральный наперстки,
# B - обменять местами правый и центральный наперстки,
# C - обменять местами левый и правый наперстки.
# Необходимо определить, под каким из наперстков окажется шарик после всех перемещений.
# INPUT.TXT записана строка длиной от 1 до 50 символов из множества {A, B, C} – последовательность перемещений.
# OUTPUT.TXT нужно вывести номер наперстка, под которым окажется шарик после перемещений.

def Seach(arr):
    for i in arr:
        if i == 'a':
            res = arr.index('a') + 1
    return res

def Calc(arr):
    data = ['a', 'b', 'c']
    for i in arr:
        if i == 'A':
            temp = data.pop(); rev = data[::-1]; data = rev + list(temp)
            res = Seach(data)
        if i == 'B':
            temp = data.pop(0); rev = data[::-1]; data = list(temp) + rev
            res = Seach(data)
        if i == 'C':
            data = data[::-1]
            res = Seach(data)
    return res


with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_678\input.txt') as input_data:
    arr = list(input_data.read())
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_678\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write('Результат: ' + str(Calc(arr)))

print(Calc(arr))