def f(arr):
    arr = list(map(int, arr.split()))
    data = []
    for i in arr:
        if i % 2 == 0:
            q = i ** 2
            data.append((i, q))
    print(data)
            
    pass

# arr = '1 2 3 5 8 15 23 38'
# f(arr)

# то же через ф - ции
def select(f, col):  # это ф-ция 'map'
    return [f(x) for x in col] 

def where(f, col):    # это ф-ция 'filter'
    return [x for x in col if f(x)] 

# data = [1, 2, 3, 5, 8, 15, 23, 38] 
# res = map(int, data)
# print(res)
# res = where(lambda x: x % 2 == 0, res) 
# print(res) # [2, 8, 38] 
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)


# Функция 'map'. Функция map() применяет указанную функцию к каждому элементу итерируемого объекта и возвращает 
# итератор с новыми объектами.

# list_1 = [x for x in range (1,20)] 
# print(list_1)
# list_1 = list(map(lambda x: x + 10, list_1 )) 
# print(list_1)


# Ф-ция 'filter'. Функция filter() применяет указанную функцию к каждому элементу итерируемого объекта и возвращает 
# итератор с теми объектами, для которых функция вернула True.

# data = [x for x in range(10)] 
# print(data)
# res = list(filter(lambda x: x % 2 == 0, data))
# print(res) # [0, 2, 4, 6, 8]

# res = list(map(lambda x: x % 2 == 0, data))
# print(res)


# Ф - ция 'zip'. Функция zip() применяется к набору итерируемых объектов и возвращает итератор с кортежами 
# из элементов входных данных.

users = ['user1', 'user2', 'user3', 'user4', 'user5'] 
ids = [4, 5, 9, 14, 7, 8, 11]  # возвр только если есть пара (8 и 11 не выводит)
data = list(zip(users, ids)) 
print(data)

users = ['user1', 'user2', 'user3', 'user4', 'user5'] 
ids = [4, 5, 9, 14, 7] 
salary = [111, 222, 333] 
data = list(zip(users, ids, salary)) 
print(data)


# Функция 'enumerate'. Функция enumerate() применяется к итерируемому объекту и возвращает новый итератор 
# с кортежами из индекса и элементов входных данных.

users = ['user1', 'user2', 'user3'] 
data = list(enumerate(users)) 
print(data)


# работа с файлами
# режим 'a'
colors = ['red', 'green', 'blue'] 
data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать data.writelines(colors) 
                             # разделителей не будет data.close()
                             
# режим 'r'
path = 'file.txt' 
data = open(path, 'r') 
for line in data: print(line) 
data.close()

# режим 'w'
colors = ['red', 'green', 'blue'] 
data = open('file.txt', 'w') 
data.writelines(colors) # разделителей не будет data.close()


# МОДУЛЬ ОС
# Модуль os предоставляет множество функций для работы с операционной системой, причем их поведение, 
# как правило, не зависит от ОС, поэтому программы остаются переносимыми.

# Базовыt функции данного модуля:
# os.chdir(path) - смена текущей директории.
import os 
os.chdir('C:/Users/79190/PycharmProjects/GB')

# os.getcwd() - текущая рабочая директория
print(os.getcwd()) 

# os.path - является вложенным модулем в модуль os и реализует некоторые полезные функции для работы с путями, такие как:
    # os.path.basename(path) - базовое имя пути
    # os.path.abspath(path) - возвращает нормализованный абсолютный путь.
    
# Модуль 'shutil' Модуль shutil содержит набор функций высокого уровня для обработки файлов, групп файлов, и папок. 
# В частности, доступные здесь функции позволяют копировать, перемещать и удалять файлы и папки. 
# Часто используется вместе с модулем os. 

import shutil
# shutil.copyfile(src, dst) - копирует содержимое (но не метаданные) файла src в файл dst. 
# shutil.copy(src, dst) - копирует содержимое файла src в файл или папку dst. 
# shutil.rmtree(path) - Удаляет текущую директорию и все поддиректории; path должен указывать на директорию, 
# а не на символическую ссылку.   