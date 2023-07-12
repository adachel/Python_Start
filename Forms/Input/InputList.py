# data = list(map(int, input().split())) # Наполнение Целыми списка в ручную

# input_data = open('D:/Works/IT/Python_Start/Tasks/Task_1/input.txt', 'r') # Забираем из файла
# data = input_data.read().split() # Разбиваем на части

# input_data = open('D:/Works/IT/Python_Start/Tasks/Task_7/input.txt', 'r') # Открываем файл
# a, b, c = map(int, input_data.read().split()) # Забираем данные и распределяем по a, b, c
# print(max(a, max(b, c))) # Ищем мах из трех

# ВВОД И ВЫВОД ЭЛЕМЕНТОВ В СПИСОК
n = int(input("Введите длину списка:"))
a = []
for i in range(0, n):
    element = int(input("Введите элемент списка:"))
    a.append(element)
print("Весь список:")
print(a)

N = int(input('Введите N: '))
print(N)
li1 = [int(input('Введите число: ')) for _ in range(N)]
print(*li1)


