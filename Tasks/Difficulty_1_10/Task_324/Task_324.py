# Требуется написать программу, определяющую, является ли четырехзначное натуральное число N палиндромом, 
# т.е. числом, которое одинаково читается слева направо и справа налево. 
# INPUT.TXT содержит натуральное число. 
# OUTPUT.TXT следует вывести слово «YES», если число N является палиндромом, или «NO» – если нет.

def Calc(n):
    for i in range(0, int(len(n) / 2)):
        if int(n[i]) - int(n[len(n) - 1 - i]) == 0:
            res = 'Yes'
        else: res = 'No'
    return res

def Dif(n):
    if len(n) < 2:
        res = 'Введите число больше "10" и меньше "-9"'
    else: res = Calc(n)
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_324\input.txt', 'r') as input_data:
    n = input_data.read()
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_324\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write(Dif(n))



print(n)
print(Dif(n))   