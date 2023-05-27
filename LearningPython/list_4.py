m = [[1,1,1], [2,2,2], [3,3,3]]
n = list(map(sum, m)) # создает список из сумм вложений

a = {sum(row) for row in m} # создает множество сумм вложений

b = {i : sum(m[i]) for i in range(3)} # создает таблицу ключей сумм

c = [ord(x) for x in 'spaam'] # спмсок порядковых чисел для символов
d = {ord(x) for x in 'spaam'} # множество с удалением дубликтов
e = {x : ord(x) for x in 'spaam'} # словарь с уникальными ключами

print(e)