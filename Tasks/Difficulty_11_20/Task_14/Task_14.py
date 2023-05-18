# В строке входного файла INPUT.TXT записаны два натуральных числа А и В через пробел, не превышающих 46340. 
# Требуется написать программу, определяющую наименьшее общее кратное (НОК) чисел a и b.
# В строку выходного файла OUTPUT.TXT нужно вывести одно целое число — НОК чисел А и В.

def Count(a, b):
    d = []
    for i in range(1, a + 1): 
        for j in range(1, b + 1):
            if a * i == b * j: d.append(i)
    d_min = min(d)
    res = a * d_min
    return res

input_data = open('D:\Works\IT\Python_Start\Tasks\Task_14\input.txt', 'r')
a, b = map(int, input_data.read().split())
input_data.close()

output_data = open('D:\Works\IT\Python_Start\Tasks\Task_14\output.txt', 'w')
output_data.write(str(Count(a, b)))
output_data.close()
print(Count(a, b))
        
        
        

       

             

