# Превод из десятичной в двоичную систему
def Binary(x):
    res = ''
    while x > 0:
        res = str(res) + str(x % 2)
        x = x // 2
    return res

def Bin(x): # Рекурсивно
    if x <= 1:
        return '1'
    else:
        res = str(x % 2) + str(Bin(x // 2))
    return res

# Превод из двоичной в десятичную
def Decimal(x):
    data = list(str(x))
    res = 0; count = 0
    for i in data:
        res = res + int(i) * (2 ** count)
        count += 1
    return res