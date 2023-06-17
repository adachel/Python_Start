# INPUT.TXT содержит две строки. В первой строке задано время отправления, а во второй строке – время в пути. 
# Время отправления задается в формате «HH:MM», где HH время в часах, которое принимает значение от 00 до 23, 
# ММ – время в минутах, которое принимает значение от 00 до 59. 
# Время в пути задается двумя неотрицательными целыми числами – количество часов и количество минут. 
# Числа разделяются одним пробелом. Количество часов не превышает 120, минут – 59.
# OUTPUT.TXT должен содержать одну строку – время прибытия поезда на конечную станцию. 
# Формат вывода этого времени совпадает с форматом ввода времени отправления.

def If(arr):
    if len(arr[0]) < 2:
        res = '0' + arr[0] + ':' + arr[1]
    else: res = arr[0] + ':' + arr[1]
    return res

def Calc(arr):
    t_otp = arr.splitlines()[0].split(':')
    t_put = arr.splitlines()[1].split()
    from datetime import timedelta
    tm3 = timedelta(hours = int(t_otp[0]), minutes = int(t_otp[1]))
    tm4 = timedelta(hours = int(t_put[0]), minutes = int(t_put[1]))
    dif = str(tm3 + tm4)
    if len(dif) > 8:
        temp = dif.split()[2].split(':')
        res = If(temp)
    elif len(dif) <= 8:
        temp = dif.split(':')
        res = If(temp)
    return res
    
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_331\input.txt') as input_data:
    arr = input_data.read()
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_331\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write('Результат: ' + Calc(arr))

print(Calc(arr))
