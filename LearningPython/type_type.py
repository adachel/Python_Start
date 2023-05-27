y = [None] * 100
a = type(y)
b = type(type(y))

if type(y) == type([]) : # Проверка типа при необходимости
    print('yes')

if type(y) == list: # Использование имени типа
    print('yes')

if isinstance (y, list) : # Объектно-ориентированная проверка
    print('yes')
    
    
    
    
print(b)