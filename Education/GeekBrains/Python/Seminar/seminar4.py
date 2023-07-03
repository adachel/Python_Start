# Задача №25. Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ уже встречался. 
# Количество повторов добавляется к символам с помощью постфикса формата _n.

def Func(arr):
    arr = arr.split()
    data = []
    count_a = 0
    count_b = 0
    count_c = 0
    count_d = 0
    for i in range(len(arr)):
        if arr[i + 1] == arr[i] == 'a': count_a += 1
        if arr[i + 1] == arr[i] == 'b': count_b += 1
        if arr[i + 1] == arr[i] == 'c': count_c += 1
        if arr[i + 1] == arr[i] == 'd': count_d += 1
    print(arr)
    
    
    
    
    pass

arr = 'a a a b c a a d c d d'
Func(arr)