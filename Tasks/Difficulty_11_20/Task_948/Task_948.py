# СТРОКИ В КНИГЕ
# В книге на одной странице помещается K строк. Таким образом, на 1-й странице печатаются строки с 1-й по K-ю, 
# на второй — с (K+1)-й по (2∙K)-ю и т.д. Напишите программу, которая по номеру строки в тексте определяет номер страницы, 
# на которой будет напечатана эта строка, и порядковый номер этой строки на странице. 
# INPUT.TXT содержит два числа через пробел: K – количество строк, которое печатается на странице, и число N – номер строки. 
# OUTPUT.TXT выведите два числа – номер страницы, на которой будет напечатана эта строка и номер строки на странице.

def Calc(arr):
    count = 0
    while arr[0] * count <= arr[1]:
        count += 1
    page = count
    line = str(arr[1] - (page - 1) * arr[0])
    res = f'{page} {line}'
    return res    
    
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_948\input.txt') as input_data:
    arr = list(map(int, input_data.read().split()))
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_948\output.txt', 'w') as output_data:
    output_data.write(Calc(arr))
    
print(Calc(arr))    