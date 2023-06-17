# a = 6
# b = 4
# print(f'{a} + {b} = {a + b}')
# print()

# БИНАРНЫЙ ПОИСК
# array = [1, 5, 9, 12, 16, 24, 39, 47, 55, 89]
# left = 0
# right = len(array) - 1
# middle = (left + right) // 2
# while left <= right:
#     middle = (left + right) // 2
#     ansver = input(f'Это число больше {array[middle]}? -- ')
#     if ansver.lower() == 'да':
#         left = middle + 1
#     elif ansver.lower() == 'нет':
#         right = middle - 1
#     else: print('Вы ответили неверно. Укажите "ДА" или "НЕТ"')
# print(array[middle])

# ПУЗЫРЬКОВАЯ СОРТИРОВКА
# array = [1, 5, 9, 12, 16, 24, 39, 47, 55, 89]
# for i in range(len(array)):
#     for j in range(len(array) - 1):
#         if array[j] > array[j + 1]:
#             temp = array[j]
#             array[j] = array[j + 1]
#             array[j + 1] = temp
# print(array)

# ИГРА НИМ
# from random import randint # ф-ция randint генерирует случайное число
n = int(input('Введите кол-во камней в куче? -- '))
count = 1
while n > 0:
    count += 1
    if count % 2 == 0:
        # comp = randint(1, 3) # Вместо этой строчки укажем ниже
        comp = n % 4  # при таких строка комп всегда выиграет 
        if comp == 0: #
            comp = 1  #
        print(f'Компьютер взял {comp} камней')
        n = n - comp
        print(f'Кол-во камней осталось - {n}')
        if n <= 0:
            print('Компьютер победил!')
    else:
        player = int(input('Введите кол-во камней от 1 до 3: '))
        while player < 1 or player > 3:
            print('Вы ошиблись!')
            player = int(input('Введите кол-во камней от 1 до 3: '))
        n = n - player
        print(f'Кол-во камней осталось - {n}')
        if n <= 0:
            print('Вы победили!')