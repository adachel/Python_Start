states = set(['1', '2', '3', '4', '5', '6', '7', '8']) # Массив преобразуется в множество
stations = {}
stations['one'] = set(['4', '5', '6'])
stations['two'] = set(['2', '4', '1'])
stations['three'] = set(['3', '5', '7'])
stations['four'] = set(['5', '6'])
stations['five'] = set(['7', '8'])
final_stations = set() # Итоговый наабор станций
while states: # Цикл повторяется до тех пор пока states_needed не станет пустым
    best_station = None # Обслуживает больше всего штаатов
    states_covered = set() # Содержит все штаты, обсл этой станцией, кот еще не входят в текущее покрытие
    for station, states_for_station in stations.items(): # Перебирает все станции и находит наилучшую
        covered = states & states_for_station # Пересечение мнежеств
        if len(covered) > len(states_covered): # Эта операция называется пересечением множеств
            best_station = station
            states_covered = covered
    final_stations.add(best_station)
    states -= states_covered
        
print(final_stations)



 