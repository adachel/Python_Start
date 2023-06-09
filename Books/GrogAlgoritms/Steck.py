def greet(name):
    print(f'Привет {name}!')
    greet2(name)
    print('готов попрощаться')
    bye()
def greet2(name):
    print(f'Как дела {name}?')
def bye():
    print('ok, пока')
name = 'Дмитрий'
print(greet(name))