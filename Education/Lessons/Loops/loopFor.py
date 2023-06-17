# for i in range(6): # Цикл от 0 до 5
#     print(i)
    
# for i in range(1, 6): # Цикл от 1 до 5
#     print(i)
    
# for i in range(1, 6, 2): # Цикл от 1 до 5 c шагом 2
#     print(i)

# for i in 'Hello world': # Перебор строки, можно так
#     print(i)

# word = 'Hello world'
# for i in word: # Перебор строки, лучше так
#     print(i)

# word = 'Hello world'
# for i in word: # По три символа
#     print(i * 3)

# word = 'Hello world!'
# for i in word: # Поиск символа в строке
#     if i == '!':
#         print('Yes')
    
# word = 'Hello world'
# count = 0
# for i in word: # Перебор строки, лучше так
#     if i == 'l':
#         count += 1   
# print('Кол-во:', count)        

# for i in range(1, 21):
#     if i == 13:
#         break # Ввыход из цикла
    
#     if i % 2 == 0: # Определяет четность
#         continue # Пропускает четные
#     print(i) # Выводит нечетные до 13

found = None
word = 'Hello'
for i in word:
    if i == 'r':
        found = True
        break # Как только символ найден, цикл остановлен
else:
    found = False
print(found)        