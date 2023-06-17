def Creat_list(n):
    from random import randint
    data = [randint(0, 100) for i in range(10)]
    print(data)
    return data

n = 10
arr = [21, 13, 98, 90, 67, 0, 13, 46, 89, 55]
print(arr)
print()
# for i in range(len(arr)):
#     index_min = arr.index(min(arr[i:]))
#     if arr[i] > arr[index_min]:
#         temp = arr[i]
#         arr[i] = arr[index_min]
#         arr[index_min] = temp
# print(arr)

# Пузырьковая сортировка
def BubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr
# print(BubbleSort(arr))

# Сортировка выбором
def SelectionSort1(arr):
    for i in range(0, len(arr)):
        index_min = i
        for j in range(i, len(arr)):
            if arr[j] < arr[index_min]:
                index_min = j
        if arr[i] > arr[index_min]:
            temp = arr[i]
            arr[i] = arr[index_min]
            arr[index_min] = temp        
    return arr

def SelectionSort2(arr):
    for i in range(len(arr)):
        a = min(arr[i:])
        index_min = arr.index(min(arr[i:]))
        if arr[i] > arr[index_min]:
            temp = arr[i]
            arr[i] = arr[index_min]
            arr[index_min] = temp
    return arr

print(SelectionSort1(arr))
# print(SelectionSort2(arr))