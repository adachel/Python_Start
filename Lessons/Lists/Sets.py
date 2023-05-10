# МНОЖЕСТВО

# data = set('hello')
# data = {5, 7, 2, 9, 1, 12, 7} # это ввод в ручную. Если нет ключей, то это множество, иначе словарь 
# # data[2] = 1 # не можем обращаться к эл-ту по индексу, не можем менять
# data.add(32) # Можно добавлять эл-ты. В начало
# data.update(['23', False, 8, 12]) # Добавляет много эл-тов
# data.remove(8) # Удаляет эл-т
# data.pop() # удаляет первый эл-т

data = [4, 7, 9, 1, 4, 8, 9] # Есть список
data = set(data) # удилил повторы и отсортировал

# data = frozenset(['qwe', 4, 'hello', 5, 7, 2, 9, 1, 12, 7, '23', False, 8, 12, 4, 7, 9, 1, 4, 8, 9]) # Неизменяемое множество

print(data) # сразу сортирует

# Примеры множеств
fruits = set(['avocado', 'tomato', 'banana']) # Фрукты: авокадо, помидор, банан
vegetables = set(['beets', 'carrots', 'tomato']) # Овощи: свекла, морковь, помидор
a = fruits | vegetables # Объединение множеств
b = fruits & vegetables # Пересечение множеств
c = fruits - vegetables # Разность множеств
d = vegetables - fruits

print(a)
print(b)
print(c)
print(d)


