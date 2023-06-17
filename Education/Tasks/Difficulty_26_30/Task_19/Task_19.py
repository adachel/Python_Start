def Arr(arr): # Зменяем символы в строке на значения индексов
    lst = []
    for i in range(0, len(arr)):
        lst.append(i)
    return lst

def Index(figura, arr_x, arr_y): # Присваиваем месту фигуры значение. Это сумма значений списков.
    for i in arr_x:
        if figura[0] == i:
            fx = x.index(i)
    for i in arr_y:
        if figura[1] == i:
            fy = y.index(i)
    return str(fx) + str(fy)

def Diag(figura, arr_x, arr_y):
    figura_mod = Index(figura, arr_x, arr_y)
    count_straight = 0
    count_revers = 0
    x_straight = Arr(arr_x)
    y_straight = Arr(arr_y)
    x_revers = Arr(arr_x)[::-1]
    y_revers = Arr(arr_y)[::-1]
    for i in x_straight:
        for j in y_straight:
            if (i + j) == figura_mod:
                count_straight += 1
    for i in x_revers:
        for j in y_revers:
            if (i + j) == figura_mod:
                count_revers += 1
    return count_straight + count_revers
    
x = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] # Ось Х
y = ['1', '2', '3', '4', '5', '6', '7', '8'] # Ось У
   
ferz = 'D4' # Положение фигуры на доске
ferz_mod = Index(ferz, x, y) # Значение фигуры
x_mod = Arr(x) # Модифицированная ось Х
y_mod = Arr(y) # Модифицированная ось У

count = 0

a = []

for i in range(x_mod[int(ferz_mod[0])], -1, -1):
    for j in range(y_mod[int(ferz_mod[1])]):
        if i == int(ferz_mod[0]):
            b = 1
            a.append(b)
            print(a)



    