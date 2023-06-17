# Подмассив массива
# INPUT.TXT содержит число 'n' - количество элементов в массиве 'а'. 
# Во второй строке содержатся числа a1, a2, … , аn разделенные пробелом. Все а[i] находятся в диапазоне от -2^31 до 2^31 - 1. 
# В третьей строке находится 'm'  — количество подмассивов, которые необходимо вывести. 
# Следующие 'm' строк содержат пары чисел i[k], j[k] (1 ≤ i[k] ≤ j[k] ≤ n).
# OUTPUT.TXT для каждой пары (i[k], j[k]) в отдельной строке выведите подмассив f(i[k], j[k]).

def Calc(arr):
    array = list(map(int, arr[1].split()))
    data = arr[3:]
    res = []
    for j in data:
        count = list(map(int, j.split()))
        temp = []
        for i in range(count[0] - 1, count[1]):
            a = array[i]
            temp.append(a)
        res.append(temp)
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_284\input.txt') as input_data:
    arr = (input_data.read().splitlines())
  
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_284\output.txt', 'w', encoding= 'utf-8') as output_data:
    for i in range(0, len(Calc(arr))):
        a = ' '.join([str(x) for x in Calc(arr)[i]])
        output_data.writelines(f'{a}\n')
    



    



