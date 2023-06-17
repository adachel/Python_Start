def Func(a, b):
    if a % b == 0:
        return b
    else:
        c = a % b; d = b
        b = c; a = d
        return Func(a, b) 
           
a = 1680
b = 640 
print(Func(a, b))   