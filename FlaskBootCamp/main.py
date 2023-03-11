from flask import Flask, render_template
from random import randint as rd

app = Flask(__name__)


@app.route('/')
def main():
    name = rd(0, 1)
    return render_template('base.html', name = name)


if __name__ == "__main__":
    app.run()




# file = open('D:/Works/IT/Python_Start/FlaskBootCamp/file.txt', 'r', encoding='utf-8')
# a - режим добавления
# w - режим записи, очищяет файл
# r - режим считывания

# list_1 = list()
# resaltData = list()
# for line in file.readlines():
    
#     resaltData.append(tuple(line.split('\n')[0].split(';')))

# file.close()
# print(resaltData)


