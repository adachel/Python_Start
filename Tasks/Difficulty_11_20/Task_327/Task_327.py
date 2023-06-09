# В одном шаге от счастья.
# INPUT.TXT содержит в первой строке число K – количество тестов. В следующих K строках записаны номера билетов. 
# Количество тестов не больше 10. Номер состоит ровно из шести цифр, среди которых могут быть и нули. 
# Гарантируется, что Вова умеет считать, то есть суммы первых трех цифр и последних трех цифр отличаются ровно на единицу.
# OUTPUT.TXT должен содержать K строк, в каждой из которых для соответствующего теста следует указать "Yes", 
# если Вова прав, и "No", если нет.

def Calc(arr):
    data = []
    arr = arr[1:]
    for i in arr:
        a = list(map(int, i[:3])); b = int(i[3:])
        if sum(a) - sum(list(map(int, str(b + 1)))) == 0 or sum(a) - sum(list(map(int, str(b - 1)))) == 0:
            res = 'Yes'
        else: res = 'No'
        data.append(res)    
    return data

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_327\input.txt') as input_data:
    arr = input_data.read().split()
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_327\output.txt', 'w', encoding= 'utf-8') as output_data:
    for i in Calc(arr): output_data.write(i + ' ')    

print(Calc(arr))