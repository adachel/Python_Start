# Hадо посчитать сумму всех чисел, на которые n делится без остатка.
def Calk(x):    # Разбиваем число на состовляющие числа
    arr = []
    for i in range(1, x + 1):
        arr.append(i)
    return arr

def Res(x, arr): # Считааем сумму чисел
    count = 0
    for i in arr:
        if x % i == 0:
            count += i
    return count
    
input_data = open('D:\Works\IT\Python_Start\Tasks\Task_23\input.txt', 'r')
num = int(input_data.read())    
input_data.close()
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_23\output.txt', 'w')
output_data.write('Result: ' + str(Res(num, Calk(num))))
    
print(Res(num, Calk(num)))