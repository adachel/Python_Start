# Внутренне имена True и False являются экземплярами типа "bool", который в свою очередь представляет собой подкласс 
# (в объектно-ориентиро­ванном смысле) встроенного целого типа int. Имена True и False ведут себя в точ­ности 
# как целые числа 1 и 0 за исключением того, что они имеют специальную логику вывода — они отображают себя 
# в виде слов True и False, а не цифр 1 и 0. В типе "bool" это достигается за счет переопределения форматов 
# строк str и герг для двух указанных объектов.

w = 1 > 2, 1 < 2 # булевые значения
r = bool('spam')

t = None # Заполнитель None
y = [None] * 100 # Инициализировать список сотней объектов None