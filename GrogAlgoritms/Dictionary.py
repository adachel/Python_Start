voted = {} # Пустой словарь
def check_voter(name):
    if voted.get(name): # get - возвращает значение, если ключ присутсвует в словаре
        print('Выгнать')
    else:
        voted[name] = True
        print('Пусть голосуют')

check_voter('Tom')
check_voter('Tom')
check_voter('Паша')
print(voted)
    
    