from flask import Flask, render_template

app = Flask(__name__)



app.route('/')
def main():
    name = 'Дмитрий'
    return render_template('D:/Works/IT/Python_Start/FlaskBootCamp/templates/base.html', name = name) # Открывает base при запуске главной страницы


if __name__=='__main__':
    app.run()


# @app.route('/')
# def main():
#     return "<h1> Hello World </h1><br><a href='/index'> перейти на вторую страницу</a>"

# @app.route('/index/<x>/<y>')
# def index(x, y):
#     return f'Результат: {int(x) + int(y)}'


# if __name__=='__main__':
#     app.run()

# //////////////////////////////////////////////////////////////////////////////////
# работа с файлом
#file = open("D:/Works/IT/Python_Start/FlaskBootCamp/file.txt", "r", encoding='utf-8')
# a - режим добавления. Если а+  и такого файла нет, то он будет создан
# w - режим на запись(очищает файл)
# r - режим считывания
# list_1 = list() # Создаем лист, это массив с разными типами данных
# resaltData = list()
# for line in file.readlines(): # проходим по каждой строке
#     resaltData.append(tuple(line.split('\n')[0].split(' '))) # делаем кортеж
# file.close()
# print(resaltData)
