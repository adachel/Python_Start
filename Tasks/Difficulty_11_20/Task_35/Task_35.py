# Однажды известный профессор обнаружил описания k конечных автоматов. По его мнению, 
# нетривиальность конечного автомата, имеющего n состояний и m переходов, 
# можно описать целым числом d = 19m + (n + 239)*(n + 366) / 2 . Чем больше d, 
# тем больший интерес для науки представляет изучение его свойств. 
# Помогите профессору вычислить нетривиальность имеющихся у него автоматов. 
# INPUT.TXT содержит целое число k – количество конечных автоматов. Следующие k строк содержат по два целых числа 
# ni и mi – число состояний и переходов i-го автомата. 
# OUTPUT.TXT должен состоять из k строк. На i-й строке выходного файла выведите одно число – нетривиальность i-го автомата.

def Calc(arr):
    data = arr[1:]
    res = []
    for i in range(0, len(data), 2):
        n = data[i]; m = data[i + 1]
        x = int(19 * m + (n + 239) * (n + 366) / 2)
        res.append(x)
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_35\input.txt', 'r') as input_data:
    arr = list(map(int, input_data.read().split()))
data = Calc(arr)  
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_35\output.txt', 'w', encoding= 'utf-8') as output_data:
    for i in data:
        output_data.write(str(i) + '\n')
    
print(data)