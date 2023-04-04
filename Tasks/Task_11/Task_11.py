def Count(data, n, k):
    for i in range(1, n + 1):
        data.append(sum(data[max(0, i - k) : i]))
    return data

input_data = open('D:\Works\IT\Python_Start\Tasks\Task_11\input.txt', 'r')
n , k = map(int, input_data.read().split())
input_data.close()
data = [1]
Count(data, n, k)
output_data = open('D:\Works\IT\Python_Start\Tasks\Task_11\output.txt', 'w')
output_data.write(str(data[n]))
print(Count(data, n, k))
print(data[n])
    

