# ПЕРЕПИСЬ
# Требуется найти номер самого старшего жителя мужского пола.
# INPUT.TXT в первой строке задано натуральное число N – количество жильцов. В последующих N строках располагается информация 
# о всех жильцах: каждая строка содержит два целых числа: V и S – возраст и пол человека. Мужскому полу соответствует 
# значение S = 1, а женскому – S = 0. 
# OUTPUT.TXT должен содержать номер самого старшего мужчины в списке. Если таких жильцов несколько, то следует вывести 
# наименьший номер. Если жильцов мужского пола нет, то выведите '-1'.

def Calc(arr):
    data = []
    for i in range(1, len(arr), 2):
        if arr[i] == 1:
            data.append(arr[i - 1])
            res = max(data)
        else: res = '-1'
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_131\input.txt') as input_data:
    arr = list(map(int, input_data.read().split()))
data = arr[1:]  
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_131\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write('Результат: ' + str(Calc(data)))

print(Calc(data))   




