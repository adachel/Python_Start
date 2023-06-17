# Требуется написать программу, которая определяет, за какую сумму предприимчивые сотрудники смогут продать весь песок 
# в случае наилучшего для себя заполнения емкостей песком. 
# Один килограмм песка первого вида они смогли бы продать за A1 рублей, второго – за A2 рублей, а третьего – за A3 рублей.
# Tри емкости: первая рассчитана на B1 килограмм, вторая на B2 килограмм, а третья на B3 килограмм. 
# Нельзя смешивать песок разных видов и заполнять емкости песком одиного видa.
# Входной файл INPUT.TXT: записано 6 натуральных чисел A1, A2, A3, B1, B2, B3. Все числа не превосходят 100.
# Выходной файл OUTPUT.TXT: вывести целое число – сумму в рублях, в случае наилучшего для себя заполнения емкостей песком.

def Calc(arr):
    n = int(len(arr) / 2)
    A = sorted(arr[:n]); B = sorted(arr[n:])
    res = 0
    for i in range(0, n):
        res = res + A[i] * B[i]
    return res
    
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_685\input.txt', 'r') as input_data:
    arr = list(map(int, input_data.read().split()))
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_685\output.txt', 'w', encoding= 'utf - 8') as output_data:
    output_data.write('Результат: ' + str(Calc(arr)))

print(Calc(arr))