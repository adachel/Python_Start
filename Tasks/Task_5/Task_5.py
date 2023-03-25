# В первой строке входного файла INPUT.TXT записано единственное число N – количество элементов целочисленного массива. 
# Вторая строка содержит N чисел, представляющих заданный массив. 
# Каждый элемент массива – натуральное число от 1 до 31. Все элементы массива разделены пробелом.

# В первую строку выходного файла OUTPUT.TXT нужно вывести числа, которые соответствуют нечетным дням месяца.
# Во второй строке соответственно расположить четные числа месяца.
# В третьей строке нужно вывести «YES», если четных больше и «NO» в противном случае.
# В каждой строчке числа следует выводить в том же порядке, в котором они идут во входных данных. 
# При выводе числа отделяются пробелом.

input_data = open('D:\Works\IT\Python_Start\Tasks\Task_5\input.txt', 'r')
N = int(input_data.readline()) # Получили первую строку - размер массива
data = input_data.readline().split(' ') # Получили вторую строку - сам массив
evenData = []; oddData = [] # Создаем два пустых списка
count_even = 0; count_odd = 0 
for i in range(0, N):
    if int(data[i]) % 2 == 0:
        evenData.append(data[i]) # Заполняем evenData
        count_even = count_even + 1
    else:
        oddData.append(data[i]) # Заполняем oddData
        count_odd = count_odd + 1
if count_even > count_odd: out = 'Yes'
else: out = 'No'
result_even = ' '.join(evenData) # Удаляем скобки и ковычки в evenData
result_odd = ' '.join(oddData)

output_data = open('D:\Works\IT\Python_Start\Tasks\Task_5\output.txt', 'w')
output_data.writelines(str(result_odd) + '\n')
output_data.writelines(str(result_even) + '\n')
output_data.writelines(out)
print(oddData)            
print(evenData)
print(out)

