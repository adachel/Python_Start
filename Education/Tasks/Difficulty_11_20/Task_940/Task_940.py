# Hаписать программу, которая удаляет из слова одну лишнюю букву. 
# INPUT.TXT содержит K - номер лишней буквы, затем через один или несколько пробелов записано слово S, 
# состоящее из английских букв верхнего регистра. Гарантируется, что номер буквы от единицы до длины слова включительно. 
# Длина слова не более 80 символов.
# OUTPUT.TXT выведите исправленное слово.

def Calc(arr):
    n = int(arr[0]); word = str(arr[1])
    word_list = list(word)
    word_list.pop(n - 1)
    res = ''.join(word_list)
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_940\input.txt') as input_data:
    arr = input_data.read().split()
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_940\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write('Правильное слово: ' + str(Calc(arr)))
    
print(Calc(arr))