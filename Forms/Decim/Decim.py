# Пример перевода в десятичное
B = '1101' # Преобразование двоичных цифр в целое число с помощью ord
I = 0
while B != '':
    I = I * 2 + (ord(B[0]) - ord('0'))
    B = B[1:]
print(I)

print(int('1101', 2))
print(bin(13))