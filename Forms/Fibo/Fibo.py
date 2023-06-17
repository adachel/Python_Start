
def Fibo(n):
    arr = [0 for x in range(0, n)]
    for i in range(0, n):
        if i < 2:
            arr[i] = 1
        elif i >= 2:
            arr[i] = arr[i - 1] + arr[i - 2]
        res = arr[n - 1]
    return res

def Fib(n):
    a = 0  # f(i - 2)
    b = 1  # f(i - 1)
    for i in range(2, n + 1): 
        a, b = b, a + b
    return b

def RecFibo(n):
    if n == 0: return 0
    if n == 1: return 1
    return RecFibo(n - 1) + RecFibo(n - 2)
    
def Iter(n):
    a = [0,1]
    for i in range(1, n):
        x = a[i] + a[i-1] 
        a.append(x)
        res = a[-1]
    return res

def Calc(n):
    if n == 1 or n == 2: return 1
    return Calc(n - 1) + Calc(n - 2)    

n = 10

print(Fibo(n))
print(Fib(n))
print(RecFibo(n))
print(Iter(n))
print(Calc(n))
        
