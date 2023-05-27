N = 5
M = 7
A = []
for i in range(N):
    A.append([1]*M) # Заполняем [1]
    
# сделать то же самое можно с помощью генератора

N = 3
M = 2
A = [ [1]*M for i in range(N) ]


# Вывод матрицы
    
for i in range(len(A)):         # len(A) - возвращает количество строк в матрице А
    for j in range(len(A[i])):  # len(A[i]) - возвращает количество элементов в строке i
        print(A[i][j], end = ' ')
    print()                     # делаем переход на новую строку   
 
print() 
    
# То же самое, но циклы не по индексу, а по значениям списка 
# (цикл for умеет делать перебор всех элементов в списке (массиве), строке):

for row in A:            # делаем перебор всех строк матрицы A
    for elem in row:     # перебираем все элементы в строке row
        print(elem, end = ' ')
    print()

print()

# Для вывода одной строки можно воспользоваться методом join:

for row in A:
    print(' '.join(list(map(str, row))))
    
# Матрица из нулей
def Matrix(n):
    arr = [0 for i in range(n)]
    matrix = [arr for x in range(n)]
    return matrix
    
def Print_Matrix(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print(arr[i][j], end= ' ')
        print()