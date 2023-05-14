# Белочка собрала в лесу N шишек c орешками. Белочка очень привередливо выбирала шишки, и брала только те, 
# в которых ровно M орешков. Также известно, что для пропитания зимой ей необходимо не менее K орешков. 
# Определите, хватит ли на зиму орешков белочке.

with open('D:\Works\IT\Python_Start\Tasks\Task_766\input.txt', 'r') as input_data:
    N, M, K = map(int, input_data.read().split())
summa = N * M
if summa >= K:
    res = 'YES'
else: res ='NO'
with open('D:\Works\IT\Python_Start\Tasks\Task_766\output.txt', 'w') as output_data:
    output_data.write('Result: ' + res)
    
print(res)