# Требуется написать программу, которая по заданным числам a и b выведет минимальное и максимальное количество цапель. 
# INPUT.TXT содержит два целых числа a и b, разделенных ровно одним пробелом. 
# OUTPUT.TXT выведите два целых числа, разделенных пробелом — минимальное и максимальное число цапель, 
# которое могло быть в вольере. Гарантируется, что хотя бы одно количество цапель соответствует условию задачи.

def Calc(arr):
    import math
    res = []
    arr = sorted(arr)
    if arr[1] / arr[0] <= 2:
        maxim = min(arr)
        minim = math.ceil(max(arr) / 2)
        res.append(minim); res.append(maxim)
    else: res = 0  
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_850\input.txt') as input_data:
    arr = list(map(int, input_data.read().split()))
if Calc(arr) == 0:
    res = 'Такого не бывает'
else: res = f'минимально: {Calc(arr)[0]}, максимально: {Calc(arr)[1]}'    
    
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_850\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write(res)
    
print(Calc(arr))

