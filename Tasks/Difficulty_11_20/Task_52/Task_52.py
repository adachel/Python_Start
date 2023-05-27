# Счастливым билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета. 
# INPUT.TXT записано шесть десятичных цифр без пробелов.  
# OUTPUT.TXT нужно вывести «YES», если билет с номером N счастливый и «NO» в противном случае.

def Calc(arr):
    sum1 = sum(arr[:3]); sum2 = sum(arr[3:])
    if sum1 == sum2:
        res = 'Yes'
    else: res = 'No'
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_52\input.txt', 'r') as input_data:
    n = int(input_data.read())
arr = [int(a) for a in str(n)] 
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_52\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write('Результат: ' + Calc(arr))  
    
print(arr)
print(Calc(arr))