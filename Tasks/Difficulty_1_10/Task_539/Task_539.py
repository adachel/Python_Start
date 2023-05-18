# Петя не знал, сколько гостей придет и разработал алгоритм, согласно которому он сможет быстро разрезать торт 
# На N равных частей. Следует учесть, что разрезы торта можно производить как по радиусу, так и по диаметру. 
# Входной файл INPUT.TXT содержит натуральное число N – число гостей, включая самого виновника торжества. 
# В выходной файл OUTPUT.TXT выведите минимально возможное число разрезов торта.

def Calc(N):
    if N % 2 == 0:
        res = int(N / 2)
    else: res = N
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_539\input.txt', 'r') as input_data:
    N = int(input_data.read())
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_539\output.txt', 'w', encoding= 'utf - 8') as output_data:
    output_data.write('Результат: ' + str(Calc(N)))   

print(Calc(N))
