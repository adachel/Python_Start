# СОРТИРОВКА ВЫБОРОМ
def find_Smallest(arr):       # Поиск индекса наименьшего элемента
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i] 
            smallest_index = i
    return smallest_index

def selectionSort(arr):       # Cортировка Выбором
    newArr = []
    for i in range(len(arr)):
        smallest = find_Smallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

data = [17, 21, 7, 10, 13, 0, 4, 26, 32, 40]
print(selectionSort(data))


