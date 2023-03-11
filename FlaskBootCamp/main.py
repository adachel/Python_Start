from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def main():
    with open('D:/Works/IT/Python_Start/FlaskBootCamp/file.txt', 'r', encoding='utf-8') as file:
        resaltData = list()    
        for line in file.readlines():
            resaltData.append(tuple(line.split('\n')[0].split(';')))
    return render_template('base.html', data = resaltData)

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == "__main__":
    app.run()

# a - режим добавления
# w - режим записи, очищяет файл
# r - режим считывания




