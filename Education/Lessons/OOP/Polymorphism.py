class Building:
    year = None
    city = None
    def __init__(self, year, city):
        self.year = year
        self.city = city
    
    def get_info(self):
        print('Year:', self.year, 'City:', self.city)
        
class School(Building): # Создаем класс, наследуем все от Building
    pupils = 0
    def __init__(self, pupils, year, city):
        super(School, self).__init__(year, city) # Обращение к init в родит классе
        self.pupils = pupils
    def get_info(self):
        super().get_info()
        print('Учеников: ', self.pupils)
class House(School): # Наследует и из Building и из School
    pass
            
# school = Building(2000, 'Moscow')
school = School(100, 2200, 'Челябинск')
school.get_info()
house = House(1, 2014, 'Питер') # Добавил третий параметр
house.get_info()
shop = Building(2015, 'Казань')
shop.get_info() 