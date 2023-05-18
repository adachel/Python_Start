# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе? 
# В единственной строке входного файла INPUT.TXT записано одно натуральное число S – общее количество сделанных журавликов. 
# В единственную строку выходного файла OUTPUT.TXT нужно вывести три числа, разделенных пробелами – количество журавликов, 
# которые сделал каждый ребенок (Петя, Катя и Сережа).

def Calc(N):
    for i in range(1, N + 1):
        if (i * 2) * 2 == (N - (i * 2)):
            temp = i
    return temp

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_92\input.txt', 'r') as input_data:
    N = int(input_data.read())
    Petr = str(Calc(N))
    Serg = str(Calc(N))
    Kat = str(Calc(N) * 2)
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_92\output.txt', 'w', encoding= 'utf - 8') as output_data:
    output_data.writelines(('Петя сделал: ' + Petr) + '\n' + ('Катя сделала: ' + Kat) + '\n' + ('Сережа сделал: ' + Serg))
    
print(Calc(N))

