def Creat_list(n):
    from random import randint
    data = [randint(0, 100) for i in range(n)]
    print(data)
    return data

def HeapSort(arr):
    for j in range(len(arr)):
        for i in range(len(arr) // 2 - j, -1, -1):
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

n = 6
arr = [35, 12, 43, 8, 51]
res = HeapSort(arr)
print(res)