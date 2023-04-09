# В строке входного файла INPUT.TXT записано два четырехзначных натуральных числа A и B через пробел, 
# где А – загаданное число, а В – предложенный вариант.
# В выходной файл OUTPUT.TXT нужно вывести два целых числа через пробел — количество быков и коров.

def Count(a, b):
    bull = 0; cow = 0
    for i in a:
        for j in b:
            if i == j and a.index(i) == b.index(j):
                bull = bull + 1
            elif i == j:
                cow = cow + 1
    return bull, cow            
    
input_data = open('D:\Works\IT\Python_Start\Tasks\Task_13\input.txt', 'r')
a, b = map(str, input_data.read().split())
input_data.close()
res = str(Count(a, b)).replace('(', '').replace(')', '').replace(',', '')
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_13\output.txt', 'w')
output_data.write(res)
output_data.close()
print(res)