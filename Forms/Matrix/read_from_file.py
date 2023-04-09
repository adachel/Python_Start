input_data = open('File.txt', 'r')
N = int(input_data.readline())
A = input_data.readlines()
Arr = [[int(n) for n in x.split()] for x in A]