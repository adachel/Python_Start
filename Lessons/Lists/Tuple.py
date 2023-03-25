# Кортеж - не изменяемый "Список"
# data = (4, 7, 9, 14, True, 78, 333, 'Hello') # У кортежа круглые скобки
# # data[6] = 6 # Кортежи не изменяемые, нельзя присвоить новое значение
# print(data[1: 6])
# print(data.count(7)) # Кол-во 7
# print(len(data)) # Длина кортежа

data = [4, 7, 9, 14, True, 78, 333, 'Hello'] # Можно без скобок
# data = (5) # Это не кортеж
# data = (5,) # Это уже кортеж
# data = 5, # Можно так
# print(data)
for i in data:
    print(i)

new_data = tuple(data) # Список в кортеж
print(new_data)
word = tuple('Hello World') # Кортеж из отдельных символов
print(word)


