graph = {} # Создаем граф
graph['Start'] = {}
graph['Start']['A'] = 6
graph['Start']['B'] = 2
graph['A'] = {}
graph['A']['Finish'] = 1
graph['A']['B'] = 3
graph['B'] = {}
graph['B']['Finish'] = 5
graph['Finish'] = {}

infinity = float('inf') # Если стоимость неизвестна, она считается беасконечной. Выражение бесконечной стоимости.
costs = {} # Таблица стоимостей
costs['A'] = 6
costs['B'] = 2
costs['Finish'] = infinity

parents = {} # Таблица родителей
parents['A'] = 'Start'
parents['B'] = 'Start'
parents['Finish'] = None

processed = [] # Для уже просмотренных элементов

def find_lowest_cost_node(costs):   # Найти узел с наименьшей стоимостью среди необработанных
    lowest_cost = float('inf') # Если стоимость неизвестна, она считается беасконечной.
    lowest_cost_node = None
    for node in costs: # Перебрать все узлы
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost # Становиться новым узлом с наименьшей стоимостью
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs) 

while node is not None: # Если обработанны все узлы, цикл завершен
    cost = costs[node]
    neighbors = graph[node]
    for n in neighbors.keys(): # Перебор всех соседей текущего узла
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost: # Если к соседу можно добраться быстрей, то
            costs[n] = new_cost # Обновит стоимость для этого узла
            parents[n] = node # Этот узел становится родителем для соседа
    processed.append(node) # Узел помечается как обрааботанный
    node = find_lowest_cost_node(costs) # Найти следующий узел и повторить цикл
     
    


