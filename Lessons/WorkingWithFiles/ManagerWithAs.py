# try:
#     file = open('ttext.txt', 'r')
#     file.read()
#     print(file)
# except FileNotFoundError:
#     print('Файл не найден!')
# finally:
#     file.close() # Выдает ошибку, т. к. переменной file здесь ужу нет
    
try:
    with open('ttext.txt', 'r') as file: # Файл открыт и будет позже закрыт
        file.read()
except FileNotFoundError:
    print('Файл не найден!')
  