# x = 0
# while x == 0:
#     try:
#         x = int(input('Введите число: '))
#         x += 5
#         print(x)
#     except ValueError: 
#         print('Введите число!')

try:
    x = 5 / 1
except ZeroDivisionError:
    print('Деление на "0"! ')
except ValueError:
    print('Введите число! ')
else:
    print('Вот так')
finally:
    print('Сработал независимо')