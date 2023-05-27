d = {'food' : 'spam', 'quantity' : 4, 'color' : 'pink'}
a = d['food'] # извлекаем значение по ключу 'food', будет 'spam'
d['quantity'] = d['quantity'] + 1 # добвить 1 к значению ключа quantity

e = {} # создаем пустой словарь
e['name'] = 'Bob'
e['work'] = 'Dev'
e['Age'] = 40 # наполняем значениями

f = dict(name = 'bob', work = 'Dev', Age = 40) # другая форма записи словаря
  
r = { 'name' : {'first' : 'Bob' , 'last' : 'Smith'}, # применение вложений
    'jobs': ['dev', 'mgr'],
    'age': 40.5}   
p = r['name']   # выводит по ключу
o = r['name']['last'] # конкретный элемент
q = r['jobs']
w = r['jobs'][-1] # вывод эл-та из вложенного списка
r['jobs'].append('janitor') # добавили эл-т в список под ключем 'jobs'

y = 'f' in r # нет эл-та 'f' в словаре r
if not 'f' in r: # проверка наличия эл-та 'f'
    print('missing')

value = r.get('x' , 0) # еще способ проверки

value = r['x'] if 'х' in r else 0 # еще способ проверки

print(value)