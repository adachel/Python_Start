# Считается, что масса толстяка должна быть не менее 94 и не более 727 килограмм. 
# Oпределить массу самого тяжелого из них, либо выяснить, что была допущена ошибка при взвешивании. 
# Входной файл INPUT.TXT содержит три целых числа M1, M2 и M3, разделенные пробелом. 
# В выходной файл OUTPUT.TXT выведите массу самого тяжелого толстяка в случае корректного взвешивания, 
# либо слово «Error» в противном случае.

def Calc(arr):
    arr_max = max(arr)
    arr_min = min(arr)
    if arr_max < 727 and arr_max > 92 and arr_min < 727 and arr_min > 92:
        res = arr_max
    else: res = 'Error'
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_754\input.txt', 'r') as input_data:
    arr = list(map(int, input_data.read().split()))
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_754\output.txt', 'w', encoding= 'utf - 8') as output_data:
    output_data.write('Результат: ' + str(Calc(arr)))
  
print(Calc(arr))
