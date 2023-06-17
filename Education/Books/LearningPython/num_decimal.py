# Десятичные числа подоб­ны числам с плавающей точкой, но имеют фиксированное количество разрядов последесятичной точки. 
# Следовательно, десятичные числа являются значениями с плаваю­щей точкой фиксированной точности.

a = 0.1 + 0.1 + 0.1 - 0.3 # НЕ РАВНО "0"!
from decimal import Decimal
b = Decimal('0.1') + Decimal('0.1') + Decimal('0.1') - Decimal('0.3') # В этом случае будет "0"
d = Decimal(0.1) + Decimal(0.1) + Decimal(0.1) - Decimal(0.3) # так не работает
c = Decimal('0.1') + Decimal('0.10') + Decimal('0.10') - Decimal('0.30')

import decimal
q = decimal.Decimal(1) / decimal.Decimal(7) #  не фикс точность
decimal.getcontext().prec = 4 # фикс точность все, что ниже
w = decimal.Decimal(1) / decimal.Decimal(7) # точность до 4 знаков

# допускается также временно сбрасыватьточность с использованием оператора диспетчера контекста with. 
# Когда происходит выход из оператора with, точность сбрасывается в свое первоначальное состояние.

import decimal
e = decimal.Decimal('1.00') / decimal.Decimal('3.00')

with decimal.localcontext() as ctx:
    ctx.prec = 2
    r = decimal.Decimal('1.00') / decimal.Decimal('3.00')

print(r)