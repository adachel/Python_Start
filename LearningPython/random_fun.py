# Стандартный библиотечный модуль random.
import random
b = random.random() # Случайные числа с плавающей точкой, целые, выбор, тасование
c = random.randint(1, 100) # случайные числа от 1 до 99

# модуль random позволяет случайным образом выбирать элемент из после­довательности и тасовать список элементов
a = random.choice(['Life of Brian', 'Holy Grail', 'Meaning of Life']) # Случайно из списка

suits = ['hearts', 'clubs' , 'diamonds', 'spades']
random.shuffle(suits) # перемешивает список




print(suits)

