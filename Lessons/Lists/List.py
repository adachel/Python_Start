# nums = [] # Пустой список
# print(nums)

# nums = [5, 6, 2, 8, 10, True, 'Hello', 6.7] # Можно указыват разные типы данных
# nums[0] = 34 # Замена элемента по индексу
# nums[5] = 'qwerty'
# print(nums[5]) # Вывод элемента по индексу

# nums = [5, 6, 2, 8, 10, True, 'Hello', 6.7, [123, 456, 444]] # Вложенный список
# print(nums[8]) # Вложенный список под индексом 8.

# nums = [5, 6, 2, 8, 10, True, 'Hello', 6.7, [123, 456, 444]]
# print(nums[-1]) # [-1] это последний элемент из списка

# nums = [5, 6, 2, 8, 10, True, 'Hello', 6.7, [123, 456, 444]] 
# print(nums[-1][1]) # Вывод элемента вложенного списка

# numbers = [134, 49, 8]
# numbers.append(112) # Добавляем элемент в список
# numbers.insert(1, True) # Вставляем доп элемент по индексу 1
# add = [123, 456]
# numbers.extend(add) # Добавляет список в конец существующего
# numbers.sort() # Сортирует список
# numbers.pop() # Удаляет последний элемент
# numbers.pop(3) # Удаляет элемент по индексу 3
# numbers.remove(True) # Удаляет элемент по значению
# # numbers.clear() # Очищает весь список
# print(numbers.count(8)) # Считает кол-во элементов со значением 8
# print(len(numbers)) # Показывает длину списка

# nums = [2, 5, 3, 10, '50', True] # False - это 0, True - это 1
# for element in nums: # Перебор списка
#     element *= 5 # Умноаем все элементы на 5
#     print(element)

n = int(input('Enter Length: ')) # Задаем длина списка
user_nums = [] # Создаем пустой список
i = 0
while i < n: # Сравнивает только с int
    string = 'Enter element: ' + str(i + 1) + ': ' # Создаем переменную string
    user_nums.append(input(string)) # Добавляем элемента в user_nums. Все элементы будут строками!!!
    i += 1
    
print(user_nums)


