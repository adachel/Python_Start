from collections import deque
def Goal(name):
    return name[-1] == 'b' # Цель поиска

def Search(name):
    search_name = deque() # Создаем пустую очередь
    search_name += graph[name] # Добавляем элементы в очередь
    search_old = [] # Уже просмотренные элементы
    while search_name:
        person = search_name.popleft() # Извлекаем персонаажа
        if not person in search_old: # Проверяем персонаажа в списке уже проверенных
            if Goal(person):
                print(person + ' - его и ищем') # Если цель найдена
                return True
            else:
                search_name += graph[person]
                search_old.append(person) # Добавляем в список уже проверенных 
    return print('Таких нет') # Таких нет
               
graph = {
'Dmitry' : ['Elena', 'Polina', 'Bogdan'],
'Elena' : ['Alla', 'Sveta', 'Misha'],
'Sveta' : ['Misha', 'Katya'],
'Polina' : ['Elmira'],
'Katya' : ['Manell'],
'Bogdan' : [],
'Alla' : [],
'Misha' : [],
'Elmira' : [],
'Manell' : []
}

Search('Dmitry')