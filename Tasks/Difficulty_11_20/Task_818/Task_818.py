# программы, которая определит максимальное число чайников, которые возможно использовать для кипячения чая, 
# используя данные тройники.
# INPUT.TXT содержится число N (1 ≤ N ≤ 105) – количество тройников. 
# Во второй строке через пробел перечислены числа a[i] (1 ≤ a[i] ≤ 1000, 1 ≤ i ≤ N) – информация о тройниках.
# OUTPUT.TXT выведите ответ на задачу.

def Calc(arr):
    temp = 0
    fin = arr[len(arr) - 1]
    for i in range(0, len(arr) - 1):
        temp += arr[i] - 1
    res = temp + fin
    return res
    
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_818\input.txt') as input_data:
    arr = list(map(int, input_data.readlines()[1:][0].split()))
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_818\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write('Результат: ' + str(Calc(arr)))
    
print(Calc(arr))