# Требуется выяснить, мимо какого наименьшего количества промежуточных станций необходимо проехать Вите по кольцу, 
# чтобы добраться с работы домой.
# INPUT.TXT заданы три числа: сначала N – общее количество станций кольцевой линии, 
# а затем i и j – номера станции, на которой Витя садится, и станции, на которой он должен выйти. 
# Станции пронумерованы подряд натуральными числами 1, 2, 3, …, N (1-я станция – соседняя с N-й), 
# N не превосходит 100. Числа i и j не совпадают. Все числа разделены пробелом.
# OUTPUT.TXT требуется вывести минимальное количество промежуточных станций (не считая станции посадки и высадки), 
# которые необходимо проехать Вите.

def Calc(arr):
    n = arr[0]; i = arr[1]; j = arr[2]
    if i < j:
        num_all = n - j + 0 + i
        num_ij = j - (i + 1)
        if num_ij < num_all:
            res = num_ij
    else:
        num_all = n - j + 0 + i
        num_ij = j - (i + 1)
        if num_ij < num_all:
            res = num_ij
    
    print(res, num_all)
    pass

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_263\input.txt') as input_data:
    arr = list(map(int, input_data.read().split()))
# with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_263\output.txt', 'w', encoding= 'utf-8') as output_data:
#     output_data.write('Результат: ' + Calc(arr))
    
Calc(arr)