from collections import deque #  для создания дву торонней очереди (дека) испоkьзуется функция 'deque'
graph = {
    'you': ['alice', 'bob', 'claire'],
    'bob': ['anuj', 'peggy'],
    'alice': ['peggy'],
    'claire': ['thom', 'jonny'],
    'anuj': [],
    'peggy': [],
    'thom': [],
    'jonny': []
}

def person_is_seller(name):
    return name[-1] == 'y'

def search(name):
    search_queue = deque() # Создаем очередь
    search_queue += graph[name] # Все соседи добавляются в очередь спискаа
    searched = [] # Массив для уже проверенных людей
    while search_queue: # Пока очередь не пуста
        person = search_queue.popleft() # Из очереди извлекается первый человек
        if not person in searched: # Проверяется, если не проверялся
            if person_is_seller(person):
                print(person + ' Да это он!') # Да это продавец
                return True
            else:
                search_queue += graph[person] # Нет не является. Все друзья добавляются в очередь.
                searched.append(person)
    return False # Если дошло до этой строки, значит в очереди нет продавца 'm' - манго

search('you')







