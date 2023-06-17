# 3а разговоры до А минут в месяц – В рублей за минуту, а разговоры сверх нормы С рублей за минуту. 
# Требуется написать программу, вычисляющую плату для разговоров продолжительностью Т минут в месяц. 
# INPUT.TXT содержит натуральные числа через пробел A, B, C и T, не превышающие 1000.
# OUTPUT.TXT выведите единственное целое число – месячную плату за пользование телефоном.

def Calc(arr):
    A = arr[0] # Норм 
    B = arr[1] # Цена за норм
    C = arr[2] # Цена сверхнорм
    T = arr[3] # Наговорили
    if T <= A:
        res = T * B
    else: res = (T - A) * C + A * B
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_933\input.txt', 'r') as input_data:
    arr = list(map(int, input_data.read().split()))
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_933\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write(f'За месяц {Calc(arr)} рублей')    
    
print(Calc(arr))