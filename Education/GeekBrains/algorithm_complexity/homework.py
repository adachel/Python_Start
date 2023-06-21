# HeapSort
def Creat_list(n):
    from random import randint
    data = [randint(0, 100) for i in range(n)]
    # print(data)
    return data

def heapify(arr, heap_size, index_i):  
    # Индекс наибольшего элемента считается корневым индексом
    largest = index_i
    left = (2 * index_i) + 1
    right = (2 * index_i) + 2

    # Если левый потомок корня — это допустимый индекс, а элемент больше,
    # чем текущий наибольший, то мы обновляем наибольший элемент
    if left < heap_size and arr[left] > arr[largest]:
        largest = left

    # То же самое и для правого потомка корня
    if right < heap_size and arr[right] > arr[largest]:
        largest = right

    # Если наибольший элемент уже не корневой, они меняются местами
    if largest != index_i:
        temp = arr[index_i]
        arr[index_i] = arr[largest]
        arr[largest] = temp
        heapify(arr, heap_size, largest)

def heap_sort(arr):  
    n = len(arr)

    # Создаём Max Heap из списка
    # 2-й аргумент означает остановку алгоритма перед элементом -1, то есть
    # перед первым элементом списка
    # 3-й аргумент означает повторный проход по списку в обратном направлении, 
    # уменьшая счётчик i на 1 
    for i in range(n//2, -1, -1):
        heapify(arr, n, i)

    # Перемещаем корень Max Heap в самый конец списка
    for i in range(n - 1, 0, -1):
        temp = arr[i]
        arr[i] = arr[0]
        arr[0] = temp
        heapify(arr, i, 0)

# Проверяем, что всё работает
# n = 60
# arr = Creat_list(n)
# heap_sort(arr)  
# print(arr)


def HeapSortMy(arr):
    for j in range(len(arr)):
        for i in range((len(arr) - j) // 2, -1, -1):
            left = (2 * i + 1); rigth = (2 * i + 2)
            if left < len(arr)-j:
                if arr[i] < arr[left]:
                    temp = arr[i]
                    arr[i] = arr[left]
                    arr[left] = temp
            if rigth < len(arr)-j:
                if arr[i] < arr[rigth]:
                    temp = arr[i]
                    arr[i] = arr[rigth]
                    arr[rigth] = temp
        temp = arr[0]
        arr[0] = arr[len(arr)-1-j]
        arr[len(arr)-1-j] = temp
    return arr

n = 60
arr = Creat_list(n)
res = HeapSortMy(arr)
print(res)