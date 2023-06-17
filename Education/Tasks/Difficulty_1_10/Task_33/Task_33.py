# Выставили на бревно несколько банок из-под кока-колы (не больше 10). 
# В единственной строке входного файла INPUT.TXT записано 2 числа — количество банок, 
# простреленных Гарри и Ларри соответственно.
# В файл OUTPUT.TXT выведите 2 числа — количество банок, не простреленных Гарри и Ларри соответственно.

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_33\input.txt', 'r') as input_data:
    a, b = map(int, input_data.read().split())
Garry = 10 - a
Larry = 10 - b
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_33\output.txt', 'w', encoding= 'utf - 8') as output_data:
    output_data.writelines(('Гарри не прострелил: ' + str(Garry)) + '\n' + ('Ларри не прострелил: ' + str(Larry)))
     
print(('Гарри не прострелил: ' + str(Garry)) + '\n' + ('Ларри не прострелил: ' + str(Larry)))