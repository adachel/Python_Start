for с in 'spam':
    print(с.upper()) # вывод в верхнем регистре
    
x = 4
while x > 0:
    print('spam ' * x)
    x -= 1
    
squares = [х ** 2 for х in [1, 2, 3, 4, 5]] # один вариант

squares = []
for х in [1, 2, 3, 4, 5]: # другой вариант
    squares.append(х ** 2)


print(squares)