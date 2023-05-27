# INPUT.TXT числа t_room и t_cond (–50 ≤ t_room ≤ 50, –50 ≤ t_cond ≤ 50). 
# OUTPUT.TXT должен содержать одно целое число — температуру, которая установится в комнате через час.

def Calc(arr):
    t_room = int(arr[0]); t_cond = int(arr[1]); temp = arr[2]
    if temp == 'heat':
        res = t_cond
    else: res = t_room
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_854\input.txt', 'r') as input_data:
    arr = list(input_data.read().split())
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_854\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write(f'В комнате установится {Calc(arr)} градусов')
        
print(Calc(arr))