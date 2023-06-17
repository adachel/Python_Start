def heapify(nums, heap_size, root_index):  
    # Индекс наибольшего элемента считается корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    # Если левый потомок корня — это допустимый индекс, а элемент больше,
    # чем текущий наибольший, то мы обновляем наибольший элемент
    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    # То же самое и для правого потомка корня
    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    # Если наибольший элемент уже не корневой, они меняются местами
    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]
        heapify(nums, heap_size, largest)

def heap_sort(nums):  
    n = len(nums)

    # Создаём Max Heap из списка
    # 2-й аргумент означает остановку алгоритма перед элементом -1, то есть
    # перед первым элементом списка
    # 3-й аргумент означает повторный проход по списку в обратном направлении, 
    # уменьшая счётчик i на 1 
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    # Перемещаем корень Max Heap в самый конец списка
    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)

# Проверяем, что всё работает
random_list_of_nums = [35, 12, 43, 8, 51]  
heap_sort(random_list_of_nums)  
print(random_list_of_nums)


# # Реализация пирамидальной сортировки на Python
# # Процедура для преобразования в двоичную кучу поддерева с корневым узлом i, что является индексом в arr[]. n - размер кучи
# def heapify(arr, n, i):
#     largest = i     # Initialize largest as root
#     l = 2 * i + 1   # left = 2*i + 1
#     r = 2 * i + 2   # right = 2*i + 2
#     if l < n and arr[i] < arr[l]:   # Проверяем существует ли левый дочерний элемент больший, чем корень
#         largest = l
#     if r < n and arr[largest] < arr[r]: # Проверяем существует ли правый дочерний элемент больший, чем корень
#         largest = r
#     if largest != i:    # Заменяем корень, если нужно
#         arr[i],arr[largest] = arr[largest],arr[i] # свап   
#         heapify(arr, n, largest)    # Применяем heapify к корню.

# def heapSort(arr):  # Основная функция для сортировки массива заданного размера
#     n = len(arr)
#     for i in range(n, -1, -1):  # Построение max-heap
#         heapify(arr, n, i)
#     for i in range(n-1, 0, -1): # Один за другим извлекаем элементы
#         arr[i], arr[0] = arr[0], arr[i] # свап 
#         heapify(arr, i, 0)

# # Управляющий код для тестирования
# arr = [8, 29, 4, 67, 3, 98]
# heapSort(arr)
# n = len(arr)
# print(arr)
# # print ("Sorted array is")
# # for i in range(n):
# #     print ("%d" %arr[i]),
# # Этот код предоставил Mohit Kumra