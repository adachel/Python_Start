# import sys # импорт модуль sys
# print(sys.platform) 
# print(2 ** 100) # возведение в степень
# x = 'Spam '
# print(x * 8) # напишет Spam восемь раз

# s = 'Spam' # строковый неизменный тип
# # s[0] = 'z' # нельзя заменить букву в строке
# s = 'z' + s[1:] # можно содать новую строку используя срез

# s = 'shrubbery'
# l = list(s) # переводим строку в список
# l[1] = 'c' # в списке меняем элемент на новый
# z = ''.join(l) # собираем список в строку уже с новым элементом

# B = bytearray(b'Spam') # bytearray поддерж изменения на месте для текста не более 8 байт
# B.extend(b'Eggs')
# r = B.decode()   # получаем SpamEggs

# s = 'spam'
# a = s.find('a') # воозвр позицию эл-та или -1 если его нет
# b = s.replace('pa', 'xyz') # новая строка sxyzm

s = 'aaa,bbb,ccc,ddd\n'
a = s.split(',') # новые строки по разделителю ','
b = s.upper() # новаая, но символы в верхнем регистре
c = s.isalpha()
d = s.isdigit()
e = s.rstrip() # удаляет пробельный символ с правой стороны
f = dir(s) # вывод всех атрибутов для строки
g = help(s.replace) # справка по replace
print(g)