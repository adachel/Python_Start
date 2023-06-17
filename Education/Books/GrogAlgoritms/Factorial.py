def Factorial(x):
    if x == 1:
        return 1
    else: 
        return x * Factorial(x - 1)
a = 10   
print(Factorial(a)) 
    