# Словарь
# country = {4: 3} # Читается как 4 это ключ к 3
# print(country[4]) # Значение по ключу

# country = {(4, 7): 3} # Ключами могут быть кортежи
# print(country[(4, 7)]) # Значение по ключу

# country = {'code': 'RU', 'name': 'Russian', 'population': 144}
# country = dict(code = 'RU', name = 'Russian', population = 144) # Другой способ записи

# for key in country: # Пробегает по ключам
#     print(key)

# for key, value in country.items(): # Пробегает и по ключам, и по элементам
#     print(key, ' - ', value)

# print(country.get('code')) # get тоже, что и квадратные скобки
# print(country.clear()) # Очищает весь словарь
# print(country.pop('code')) # Удаляет элемент с ключом code
# print(country.popitem()) # Удаляет последний элемент
# print(country.keys()) # Только ключи
# print(country.values()) # Только значения
# print(country.items()) # Ключ и значение как отдельный кортеж
# country['code'] = 'None' # Новое значение по ключу
# print(country)

person = {
    'user_1': {
        'first_name': 'Дмитрий',
        'last_name': 'Аржевитин',
        'age': 48,
        'address': ('г. Челябинск', 'ул. Какая-то', '№ - 15', 'квартира', '2'),
        'grades': {'math': 5, 'physics': 3}
    },
    'user_2': { 
    }
}
print(person['user_1']['address'][1])




