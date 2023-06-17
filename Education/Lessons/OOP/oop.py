class Cat_one:          # Создаем класс с параметрами name, age, isHappy
    name = None
    age = None
    isHappy = None
    
Cat1_one = Cat_one()        # Создаем объект на основе хар-к класса
Cat1_one.name = 'Барсик'
Cat1_one.age = 3
Cat1_one.isHappy = True

Cat2_one = Cat_one()        # Создаем объект на основе хар-к класса
Cat2_one.name = 'Жопен'
Cat2_one.age = 2
Cat2_one.isHappy = True

print(Cat1_one.name)
print(Cat2_one.name) 

print()

class Cat_two:
    name = None
    age = None
    isHappy = None
    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy
        
Cat1_two = Cat_two()
Cat1_two.set_data('Барсик', 3, True)

Cat2_two = Cat_two()
Cat2_two.set_data('Жопен', 2, False)

print(Cat1_two.name)
print(Cat2_two.name)

print()

class Cat_three:
    name = None
    age = None
    isHappy = None
    def set_data(self, name, age, isHappy):
        self.name = name
        self.age = age
        self.isHappy = isHappy
    def get_data(self):
        print(self.name, 'age', self.age, '. Happy', self.isHappy)

Cat1_three = Cat_three()
Cat1_three.set_data('Барсик', 3, True)
Cat2_three = Cat_three()
Cat2_three.set_data('Жопен', 2, False)

Cat1_three.get_data()
Cat2_three.get_data()
