# INPUT.TXT содержит число К – количество кубиков. 
# OUTPUT.TXT выведите количество кубиков в последней ступеньке у максимально высокой лестницы, 
# которую можно построить из K кубиков.

def Calc(n):
    a = 0
    arr = []
    for i in range(0, n):
        for j in range(0, i + 1):
            a = i 
            arr.append(a)
    res = arr[n]
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_514\input.txt') as input_data:
    n = int(input_data.read())
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_514\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write('Результат: ' + str(Calc(n)))
    
print(Calc(n))
