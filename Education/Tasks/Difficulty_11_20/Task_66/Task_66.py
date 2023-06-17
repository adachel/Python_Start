# Для данной буквы английского алфавита нужно вывести справа стоящую букву на стандартной клавиатуре. 
# При этом клавиатура замкнута, т.е. справа от буквы «p» стоит буква «a», от буквы «l» стоит буква «z», 
# а от буквы «m» — буква «q». INPUT.TXT содержит один символ — маленькую букву английского алфавита. 
# OUTPUT.TXT следует вывести букву стоящую справа от заданной буквы, с учетом замкнутости клавиатуры.

def Calc(n, arr):
    for i in range(0, len(arr)):
        if n == 'm':
            res = 'q'
        elif arr[i] == n:
            res = arr[i + 1]
    return res
            
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_66\input.txt', 'r') as input_data:
    n = input_data.read()
arr = 'qwertyuiopasdfghjklzxcvbnm'
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_66\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write('Результат: ' + Calc(n, arr))
print(Calc(n, arr))