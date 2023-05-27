# Побитовые операции
x = 1 # Десятичное значение 1 в битах выглядит как 0001
a = x << 2 # Сдвиг влево на 2 бита: 0100. Двоичная 1 (по основанию 2, 0001) сдвигается влево на две позиции, чтобы породить двоичную 4 (0100).
b = x | 2 # Побитовое ИЛИ (один из битов = 1) : 0011
c = x & 1 # Побитовое И (оба бита = 1) : 0001

x = 0b0001 # Двоичные литералы
q = x << 2 # Сдвиг влево
w = bin(x << 2) # Строка двоичных цифр
e = bin(x | 0b010) # Побитовое ИЛИ: один из битов = 1
r = bin(x & 0b1) # Побитовое И: оба бита = 1

y = 0xFF # Шестнадцатеричные литералы
i = bin(y)
o = y ^ 0b10101010 # Побитовое исключающее ИЛИ: один из битов = 1, но не оба
j = bin(o)
g = int(j, 2) # Цифры => число: строка в целое по указанному основанию
l = hex(g) # Число => цифры: строка шестнадцатеричных цифp


# ме­тод bit__length, который позволяет запрашивать количество битов
m = 99
n = bin(m) , m.bit_length() , len(bin(m)) - 2

v = bin(256), (256).bit_length() , len(bin(256)) - 2

print(v)

