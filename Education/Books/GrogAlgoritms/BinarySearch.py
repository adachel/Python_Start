# БИНАРНЫЙ ПОИСК
def binary_search(array, item):
    low = 0 
    high = len(array) - 1
    while low <= high:
        mid = (low + high)
        guess = data[mid] 
        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else: low = mid + 1
    return None
data = [1, 4, 7, 10, 13, 17, 21, 26, 32, 40]
print(binary_search(data, 13))