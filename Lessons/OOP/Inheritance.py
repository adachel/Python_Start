class Building:
    year = None
    city = None
    def __init__(self, year = None, city = None):
        self.year = year
        self.city = city
    
    def get_info(self):
        print('Year:', self.year, 'City:', self.city)
        
class School(Building): # Создаем класс, наследуем все от Building
    pupils = 0
    def __init__(self, pupils = None, year = None, city = None):
        super(School, self).__init__(year, city) # Обращение к init в родит классе
        self.pupils = pupils
class House(School): # Наследует и из Building и из School
    pass
            
# school = Building(2000, 'Moscow')
school = School(100, 2200, 'Челябинск')
school.get_info() # Чтоб вывести pupols смотрим ПОЛИМОРФИЗМ
house = House(1, 2014, 'Питер') # Добавил третий параметр