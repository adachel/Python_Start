# Строка
# word = 'Business' # Без скобок
# print(word[5]) # Показываем 5 элемент
# print(len(word)) # Кол-во элементов в слове
# print(word.count('s')) # Показывает кол-во 's' в слове
# print(word.upper()) # Показывает строку в верхнем регистре
# word = word.upper()
# print(word.upper()[5]) # Показал только 5 элемент в верхнем регистре
# print(word.isupper()) # Показывает, элементs в верхнем регистре? False или True 
# print(word.islower()) # Обратная isupper
# word = word.lower() # Весь текст в нижний регистр
# print(word.capitalize()) # Только первая заглавная, ост в нижнем
# print(word.find('i')) # Индекс искомого элемента
# print(word.split('i')) # Разбивает строку по элементу 'i'.

word = 'Football, basketball, skate' # Есть текст
hobby = word.split(', ') # Разбиваем на элементы по ", прбел"
for i in range(len(hobby)): # Проходим по элемента до конца списка
    hobby[i] = hobby[i].capitalize() # Применяем к элементам метод capitalize
result = ', '.join(hobby) # Склеиваем элементы в одно по ", пробел"
print(result) # Результат


