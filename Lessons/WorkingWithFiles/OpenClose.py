# file = open('text.txt', 'w') # Создался в корневой папке репозитория 'w' - записть каждый раз новая
# file.write('Hello\n')
# file.write('!!!')
# file.close()

file = open('text.txt', 'a') # 'a' - добавляет к существующей
file.write('Hello\n')
file.write('!!!')
file.close()

file = open('text.txt', 'r') # 'r' - считывание
# print(file.read(3)) # Читает только 3 символа
for line in file: # Чтение по строке из файла
    print(line, end='')

file.close()


