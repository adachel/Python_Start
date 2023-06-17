# Заданы первый и второй элементы арифметической прогрессии. Требуется написать программу, 
# которая вычислит элемент прогрессии по ее номеру. 
# INPUT.TXT содержит три целых числа, разделенных пробелами – первый элемент прогрессии A1 (1 ≤ A1 ≤ 1000), 
# второй элемент прогрессии A2 (1 ≤ A2 ≤ 1000), и номер требуемого элемента N (1 ≤ N ≤ 1000). 
# OUTPUT.TXT должен содержать одно целое число - N-й элемент арифметической прогрессии.

def Calc(arr):
    A1 = arr[0]; A2 = arr[1]; k = arr[2]
    D = A2 - A1
    res = A1 + (k - 1) * D
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_312\input.txt') as input_data:
    arr = list(map(int, input_data.read().split()))
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_312\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write('Результат: ' + str(Calc(arr)))
    
print(Calc(arr))   

    
    



