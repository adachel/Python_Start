# СОРТИРОВКА КЛЮЧЕЙ

d = {'l' : 1, 'd' : 2, 'c' : 3}
ks = list(d.keys()) # не сортированный список ключей
ks.sort() # отсортированный список ключей

for key in ks:
    print(key, '=>', d[key])   # Проход по отсортированным ключам
    
for key in sorted(d) :
    print(key, '=>', d[key])




print(ks)
