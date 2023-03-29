# Если пользователь вводит значение «C7-D5», то программа должна определить это как правильный ход, 
# Если же введено «E2-E4», то ход неверный. Также нужно проверить корректность записи ввода: 
# Если например, введено «D9-N5», то программа должна определить данную запись как ошибочную. 
# В единственной строке входного файла INPUT.TXT записан текст хода (непустая строка), который указал пользователь. 
# Пользователь не может ввести строку, длиннее 5 символов.
# В выходной файл OUTPUT.TXT нужно вывести «YES», если указанный ход конем верный, 
# Eсли же запись корректна (в смысле правильности записи координат), но ход невозможен, 
# Tо нужно вывести «NO». Если же координаты не определены или заданы некорректно, то вывести сообщение «ERROR».

# input_data = open('D:\Works\IT\Python_Start\Tasks\Task_6\input.txt', 'r')
# data = input_data.read().split('-')
# letter_1 = data[0]
# letter_2 = data[1]
# data_x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# n_x = len(data_x)
# for i in range(0, n_x):
#     data_y = ['1', '2', '3', '4', '5', '6', '7', '8']
#     n_y = len(data_y)
#     for j in range(0, n_y):
#         if letter_1 == data_x[i] + data_y[j]:
#             letter_1 = str(i) + str(j)
#         if letter_2 == data_x[i] + data_y[j]:
#             letter_2 = str(i) + str(j)       
# dif = int(letter_2) - int(letter_1)
# if abs(dif) == 8 or abs(dif) == 12 or abs(dif) == 19 or abs(dif) == 21:
#     out = 'Yes'
# else:
#     out = 'No'
# print(dif)
# print(out)
# print(error)        
     
# input_data = open('D:\Works\IT\Python_Start\Tasks\Task_6\input.txt', 'r')
# data = input_data.read()
# i_data = list(data)
# data_x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
# for i in data_x:
#     if i_data[0] == i:
#         i_data[0] = data_x.index(i)
#     if i_data[3] == i:
#         i_data[3] = data_x.index(i)
# if len(data) > 5 or data[0] < 'A' or data[3] < 'A' or data[0] > 'H' or data[3] > 'H':
#     out = 'ERROR'
# elif data[2] != '-' or int(data[1]) < 1 or int(data[4]) < 1 or int(data[1]) > 8 or int(data[4]) > 8:
#     out = 'ERROR'
# elif (abs(i_data[0] - i_data[3]) * abs(int(i_data[1]) - int(i_data[4]))) == 2:
#     out = 'Yes'
# else: out = 'No'
# output_data = open('D:/Works/IT/Python_Start/Tasks/Task_6/output.txt', 'w')
# output_data.write(out)
# print(out)

def Indexes(arr):
    data = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    for i in data:
        if arr[0] == i:
            a = data.index(i)
        if arr[3] == i:
            b = data.index(i)
    data_index = str(a) + str(b)
    return data_index
def Comparison(arr, arr_index):
    if len(arr) > 5 or arr[0] < 'A' or arr[3] < 'A' or arr[0] > 'H' or arr[3] > 'H':
        out = 'ERROR'
    elif arr[2] != '-' or int(arr[1]) < 1 or int(arr[4]) < 1 or int(arr[1]) > 8 or int(arr[4]) > 8:
        out = 'ERROR'
    elif (abs(arr_index[0] - arr_index[1]) * abs(int(arr[1]) - int(arr[4]))) == 2:
        out = 'Yes'
    else: out = 'No'
    return out
input_data = open('D:\Works\IT\Python_Start\Tasks\Task_6\input.txt', 'r')
data = input_data.read()
data_index = list(map(int, Indexes(data)))
result = Comparison(data, data_index)
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_6\output.txt', 'w')
output_data.write(str(result))
print(result)










