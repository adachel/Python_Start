def f(n):
    a = [1] + [0] * n
    
    for i in range(1, n + 1):
        for j in range(n, i - 1, - 1):
            a[j] += a[j - i]
            
    return max(a) 
print(f(int(input())))       
            