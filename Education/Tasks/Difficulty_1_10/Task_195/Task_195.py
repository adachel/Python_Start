# Hа обработку одного квадратного метра требуется 1 нанограмм сульфида. 
# Всего необходимо обработать N прямоугольных панелей размером A на B метров. 
# Hеобходимо подсчитать, сколько всего сульфида необходимо на обработку всех панелей. 
# Панели требуют обработки с обеих сторон.

with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_195\input.txt', 'r') as input_data:
    N, A, B = map(int, input_data.read().split())
    p = ((A * B) * 2) * N # Площадь всего
    sulf = p * 1 # Сульфидаа на площадь
with open('D:\Works\IT\Python_Start\Tasks\Difficulty_1_10\Task_195\output.txt', 'w', encoding= 'utf - 8') as output_data:
    output_data.write('Результат: ' + str(sulf))
    
print(p)