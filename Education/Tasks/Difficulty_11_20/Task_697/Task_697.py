# Cколько в действительности банок краски необходимо для покраски стен в офисе длиной L метров, 
# шириной – W и высотой – H, если одной банки хватает на 16м2, а размерами дверей и окон можно пренебречь? 
# Hаписать программу, которая будет все это считать. 
# INPUT.TXT содержит три натуральных числа L, W, H через пробел – длину, ширину и высоту офиса в метрах соответственно. 
# OUTPUT.TXT выведите одно целое число – минимальное количество банок краски, необходимых для покраски стен в офисе.

def Calc(arr):
    L = arr[0]; W = arr[1]; H = arr[2]
    S = L * H * 2 + W * H * 2
    res = round(S / 16)
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_697\input.txt', 'r') as input_data:
    arr = list(map(int, input_data.read().split()))
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_697\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write(f'Нужно {Calc(arr)} банок краски')

print(Calc(arr))

