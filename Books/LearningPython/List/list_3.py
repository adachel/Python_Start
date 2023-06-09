a = list(range(4)) # создаем список при помощи range
b = list(range(-6, 15, 2)) # список от -6 до 15 с шагом 2

c = [[x ** 2, x ** 3] for x in range(4)] # создаем матрицу. Перв элем это квадрт, втор это в кубе
d = [[x, int(x / 2), x * 2] for x in range(-6, 9, 2) if x != 0] # матр 3х6. range это кол-во стpok с элем с -6
e = [[x, x, x] for x in range(4)] # кол-во x это кол-во столбцов

m = [[1,1,1], [3,2,2], [3,3,3]]
g = (sum(row) for row in m) 
r1 = next(g) # выводит сумму 1 вложения
r2 = next(g) # выводит сумму 2 вложения
r3 = next(g) # выводит сумму 3 вложения

print(r3)