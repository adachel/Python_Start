# Змейка
# def Matrix(arr): # ver. 1
#     n = arr[0]; m = arr[1]
#     data = []
#     a = 0; c = 0
#     for i in range(n):
#         temp = []
#         if i == 0:
#             b = a + c
#             for j in range(m):
#                 c = 1; a = j + b
#                 temp.append(a)
#         elif i > 1 and i % 2 == 0:
#             b = d + c
#             for j in range(m):
#                 c = 1; a = j + b
#                 temp.append(a)
#         else:
#             b = a + c
#             for j in range((m - 1), -1, -1):
#                 c = 1; a = b + j
#                 temp.append(a)
#                 d = temp[0]       
#         data.append(temp)
#     return data

def Matrix(arr): #ver. 2
    n = arr[0]; m = arr[1]
    matrix = []
    for j in range(n):
        if j == 0:
            data = [i + j for i in range(m)]
            a = data[-1] + m
        elif j % 2 == 1:
            data = [a - i for i in range(m)]
            b = data[0] + 1
        elif j % 2 == 0 and j > 1:
            data = [i + b for i in range(m)]
            a = data[-1] + m
        matrix.append(data)
    return matrix
