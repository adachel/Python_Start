def QickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
    return QickSort(less) + [pivot] + QickSort(greater)
arr = [2, 1, 6, 3, 5, 12, 65, 34, 22, 10]
print(QickSort(arr))

def F(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = len(arr) // 2
        less = [i for i in arr if i < arr[pivot]]
        greater = [i for i in arr if i > arr[pivot]]
    return  F(less) + [arr[pivot]] + F(greater)
print(F(arr))
    
    
    