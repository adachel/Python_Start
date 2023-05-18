# Дано натуральное число N и последовательность из N элементов. Требуется вывести эту последовательность в обратном порядке. 
# В первой строке входного файла INPUT.TXT записано натуральное число N. 
# Во второй строке через пробел идут N целых чисел - элементы последовательности. 
# В выходной файл OUTPUT.TXT выведите заданную последовательность в обратном порядке.

def Calc(arr):
    res = arr[::-1]
    return res
    
def Rev(arr):
    for i in range(0, int(len(arr) / 2)):
        temp = arr[i]
        arr[i] = arr[len(arr) - 1]
        arr[len(arr) - 1] = temp
    return arr

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_149\input.txt', 'r') as input_data:
    arr = input_data.readlines()
    arr = list(map(int, arr[1].split()))
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_149\output.txt', 'w', encoding= 'utf - 8') as output_data:
    output_data.write(str(Calc(arr)))
      
print(Calc(arr))
print(Rev(arr))