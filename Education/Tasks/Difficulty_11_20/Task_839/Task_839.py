# INPUT.TXT содержит непустую последовательность из нулей и единиц. Длина последовательности.  
# OUTPUT.TXT выведите слово «YES», если факт был известен всем опрошенным людям, и слово "NO" в противном случае.

def Calc(arr):
    for i in range(0, len(arr)):
        if arr[i] == 0:
            res = 'No'
            break
        else: res = 'Yes'
    return res

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_839\input.txt') as input_data:
    arr = list(input_data.read())
    arr_int = [int(x) for x in arr]
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_11_20\Task_839\output.txt', 'w', encoding= 'utf-8') as output_data:
    output_data.write('Результат: ' + Calc(arr_int))
  
print(Calc(arr_int))
    
