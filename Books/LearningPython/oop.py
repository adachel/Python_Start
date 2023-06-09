# В общих поня­тиях классы определяют новые типы объектов

class Worker:
    def __init__(self, name, pay): # Инициализировать при создании
        self .name = name # self - новый объект
        self .pay = pay
    def lastName(self) :
        return self.name.split()[-1] # Разбить строку по пробелам
    def giveRaise(self, percent):
        self.pay *= (1.0 + percent) # Обновить pay на месте
        
# Класс Worker определяет новый вид объекта, который будет иметь атрибуты name и pay (иногда называемые информацией о состоянии), 
# а также две линии поведения, реализованные как функции (обычно называемые методами).

bob = Worker('Bob Smith', 50000) # Создать два экземпляра
sue = Worker('Sue Jones', 60000) # Каждый имеет атрибуты name и pay

print(bob.lastName()) # Вызвать метод: bob - это self
print(sue.lastName()) # sue - это self

sue.giveRaise(.10) # Обновить атрибут pay в экземпляре sue
print(sue.pay)





