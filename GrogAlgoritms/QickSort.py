def QickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
    return QickSort(greater) + [pivot] + QickSort(less)
arr = [2, 1, 6, 3, 5, 12, 65, 34, 22, 10]
print(QickSort(arr))

    
    
    