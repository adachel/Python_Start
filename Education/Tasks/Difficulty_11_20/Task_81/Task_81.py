# INPUT.TXT задано одно число N – количество арбузов. Вторая строка содержит N чисел, записанных через пробел. 
# Здесь каждое число – это масса соответствующего арбуза. Все числа натуральные и не превышают 30000.
# OUTPUT.TXT нужно вывести два числа через пробел: массу арбуза, который Иван Васильевич купит теще и массу арбуза, 
# который он купит себе.

def Calc(arr):
    arr_sort = sorted(arr)
    IB = max(arr)
    new_arr = arr[:-1]
    t = max(new_arr)
    res = f'Теще арбуз {t} кг, себе {IB} кг'
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_81\input.txt') as input_data:
    arr = list(map(int, input_data.readlines()[1:][0].split()))
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_81\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write(Calc(arr))

print(Calc(arr))