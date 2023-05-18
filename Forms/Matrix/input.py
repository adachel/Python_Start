# Считываем матрицу из файла
data = []
with open('Путь к файлу txt', 'r') as input_data:
    for line in input_data:
        data.append([int(x) for x in line.split()])

# Заполнение матрицы значениями с клавиатуры

n = 5
A = []
for i in range(n):
    A.append(list(map(int, input().split())))   # метод list() создает список(массив) 
                                                # из набора данных, указанных в скобках
                                                
print()                                         
       
# Или, без использования сложных вложенных вызовов функций:

B = []
for i in range(n):
    row = input().split()      # считали строку с числами, 
                               # разбили на элементы по пробелам (получили массив row)
    for i in range(len(row)):
        row[i] = int(row[i])   # каждый элемента списка row преобразовали в число
    B.append(row)              # добавили массив row к массиву A   
    
    
print(A)
print()
print(B)    
    