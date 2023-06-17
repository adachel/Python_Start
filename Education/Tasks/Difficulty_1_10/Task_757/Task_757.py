# По заданному количеству атомов каждого из описанных выше элементов требуется определить 
# максимально возможное количество молекул спирта, которые могут образоваться в процессе их соединения. 
# INPUT.TXT содержит 3 натуральных числа: C, Н и O – количество атомов углерода, водорода и кислорода соответственно. 
# OUTPUT.TXT выведите максимально возможное число молекул спирта, которые могут получиться из атомов, 
# представленных во входных данных.

def Calc(arr):
    base = [2, 6, 1]
    count = 0
    while (arr[0] - base[0]) >= 0 and (arr[1] - base[1]) >= 0 and (arr[2] - base[2]) >= 0:
        arr[0] = arr[0] - base[0]; arr[1] = arr[1] - base[1]; arr[2] = arr[2] - base[2]
        count += 1 
    res = count
    return res

def Count(arr):
    base = [2, 6, 1]
    lst = []
    for i in range(0, len(arr)):
        c = arr[i] // base[i]
        lst.append(c)
    res = min(lst)
    return res   
   

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_757\input.txt', 'r') as input_data:
    data = list(map(int, input_data.read().split()))
    arr = tuple(data)
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_757\output.txt', 'w', encoding= 'utf - 8') as output_data:
    output_data.write('кол-во молекул: ' + str(Count(arr)))

# print(Calc(data))
print(Count(arr))