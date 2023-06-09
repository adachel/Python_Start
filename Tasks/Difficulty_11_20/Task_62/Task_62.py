# INPUT.TXT записана координата клетки на шахматной доске: всего два символа – буква и цифра (без пробелов).
# OUTPUT.TXT нужно вывести «WHITE», если указанная клетка имеет белый цвет и «BLACK», если она черная.

def Calc(arr):
    data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    for i in data:
        if i == arr[0]: 
            if data.index(i) % 2 == 0 and int(arr[1]) % 2 == 0:
                res = 'White'
            elif data.index(i) % 2 != 0 and int(arr[1]) % 2 != 0:
                res = 'White'
            else: res = 'Black'
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_62\input.txt') as input_data:
    arr = list(input_data.read())
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_62\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write('Результат: ' + Calc(arr))

print(Calc(arr))