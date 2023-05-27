with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_52\input.txt', 'r') as input_data:
    n = int(input_data.read())

arr = [int(a) for a in str(n)] 

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_81\input.txt') as input_data:
    arr = list(map(int, input_data.readlines()[1:][0].split())) # забираем со второй строки и сразу в список int
