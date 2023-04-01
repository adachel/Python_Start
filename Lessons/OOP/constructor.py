class Cat_three:
    name = None
    age = None
    isHappy = None
    def __init__(self, name, age, isHappy): # Это констректор (__init__ обязательно). Упрощает код.
        self.name = name
        self.age = age
        self.isHappy = isHappy
    def set_data(self, name, age, isHappy): # От этого метода можно избавиться
        self.name = name
        self.age = age
        self.isHappy = isHappy
    def get_data(self):
        print(self.name, 'age', self.age, '. Happy', self.isHappy)

Cat1_three = Cat_three('Барсик', 3, True)
Cat2_three = Cat_three('Жопен', 2, False)

Cat1_three.get_data()
Cat2_three.get_data()

print()

class Cat_four:
    name = None
    age = None
    isHappy = None
    def __init__(self, name, age, isHappy): # Это констректор (__init__ обязательно). Упрощает код.
        self.name = name
        self.age = age
        self.isHappy = isHappy
        self.set_data(name, age, isHappy)
        self.get_data()                     # Прям в теле формирует вывод нового объекта
    def set_data(self, name, age, isHappy): # От этого метода можно избавиться
        self.name = name
        self.age = age
        self.isHappy = isHappy
    def get_data(self):
        print(self.name, 'age', self.age, '. Happy', self.isHappy)

Cat1_four = Cat_four('Барсик', 3, True)
Cat2_four = Cat_four('Жопен', 2, False)
Cat3_four = Cat_four('Мурка', 4, True) # Просто добавили новый объект

print()

class Cat_five:
    name = None
    age = None
    isHappy = None
    def __init__(self, name = ['Можно список и др'], age = None, isHappy = None): # Переопределение параметров
        self.name = name
        self.age = age
        self.isHappy = isHappy
        self.set_data(name, age, isHappy)
        self.get_data()                     # Прям в теле формирует вывод нового объекта
    def set_data(self, name = None, age = None, isHappy = None): 
        self.name = name
        self.age = age
        self.isHappy = isHappy
    def get_data(self):
        print(self.name, 'age', self.age, '. Happy', self.isHappy)

Cat1_five = Cat_five('Барсик', 3, True)
Cat2_five = Cat_five('Жопен', 2, False)
Cat3_five = Cat_five('Мурка', 4, True) # Просто добавили новый объект
Cat4_five = Cat_five('Мурзик', 1)      # Теперь можно задавать меньше параметров
Cat5_five = Cat_five()



