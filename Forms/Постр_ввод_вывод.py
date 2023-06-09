def Calc(arr):
    pass

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_284\input.txt') as input_data:
    arr = (input_data.read().splitlines())

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_284\output.txt', 'w', encoding= 'utf-8') as output_data:
    for i in range(0, len(Calc(arr))):
        a = ' '.join([str(x) for x in Calc(arr)[i]])
        output_data.writelines(f'{a}\n')