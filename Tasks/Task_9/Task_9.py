# В первой строке INPUT.TXT записано число N – количество элементов массива. Вторая строка содержит N целых чисел,
# представляющих массив. Все элементы разделены пробелом. Каждое из чисел во входном файле не превышает 10^2.
# В строку OUTPUT.TXT вывести два числа, разделенных пробелом: 
# сумму положительных элементов и произведение чисел, расположенных между минимальным и максимальным элементами. 

# input_data = open('D:\Works\IT\Python_Start\Tasks\Task_9\input.txt', 'r')
# N = input_data.readline()
# data = input_data.readline().split()
# data_int = [int(x) for x in data] # Перевод списки строковых чисел в числовой список
# summa = 0; mul = 1
# data_min = min(data_int) # Находin в списим mке
# data_max = max(data_int) # Находим max 
# i_min = data_int.index(data_min) # Находим индекс min элемента
# i_max = data_int.index(data_max) # Находим индекс max элемента
# if i_min < i_max:
#     for i in range(i_min + 1, i_max):
#         mul = mul * data_int[i]
# else:
#     for i in range(i_max + 1, i_min):
#         mul = mul * data_int[i]
# for i in data:
#     if int(i) >= 0:
#         summa = summa + int(i)
# output_data = open('D:\Works\IT\Python_Start\Tasks\Task_9\output.txt', 'w')
# output_data.writelines(str(summa) + '\n')
# output_data.writelines(str(mul) + '\n')
# print(data_int)
# print(summa)
# print(mul)

def iMin(data):
    int_data = [int(x) for x in data]
    minNum = min(int_data)
    imin = int_data.index(minNum)
    return imin
def iMax(data):
    int_data = [int(x) for x in data]
    maxNum = max(int_data)
    imax = int_data.index(maxNum)
    return imax
def Mult(data, imin, imax):
    mult = 1
    int_data = [int(x) for x in data]
    if imin < imax:
        for i in range(imin + 1, imax):
            mult = mult * int_data[i]
    else:
        for i in range(imax + 1, imin):
            mult = mult * int_data[i]
    return mult
def Summa(data):
    summa = 0
    for i in data:
        if int(i) >= 0:
            summa = summa + int(i)
    return summa
input_data = open('D:\Works\IT\Python_Start\Tasks\Task_9\input.txt', 'r')
N = input_data.readline()
data = input_data.readline().split()
imin = iMin(data)
imax = iMax(data)
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_9\output.txt', 'w')
output_data.write(str(Summa(data)) + ' ')
output_data.write(str(Mult(data, imin, imax)))
print(Mult(data, imin, imax))
print(Summa(data))







