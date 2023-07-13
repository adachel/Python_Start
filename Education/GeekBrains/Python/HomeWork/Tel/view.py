def Input_Num():
    ask = int(input("Выбери действие:\n1 - Записать нового пользователя\n2 - Найти пользователя\n3 - Отсортировать\n4 - Удаление пользователя\n5 - Переименование\n6 - Вывести всех пользователей\n7 - Выход из программы\n    Введите: "))
    return ask

def Input_Name():       
    id = input('Введите ID: ')
    name = input('Введите ФИО: ')
    telephone = input('Ведите телефон: ')
    res = id + ',' + name + ',' + telephone + '\n'
    return res

def Input_Name1():       
    id = input('Введите ID: ')
    name = input('Введите ФИО: ')
    telephone = input('Ведите телефон: ')
    res = id + ',' + name + ',' + telephone
    return res
    
def Input_Char():       
    char = int(input('Введите характерстику:\n1 - по ID\n2 - по Фамилии\n3 - по Имени\n4 - по Телефону\n  Введите: '))
    return char

def Input_ID():         
    ID = (input('Введите ID: '))
    return ID

def Input_LastName():    
    lastName = input('Введите Фамилию: ')
    return lastName

def Input_FirstName():  
    firstName = input('Введите Имя: ')
    return firstName
    
def Input_Phone():
    phone = (input('Введите телефон: '))
    return phone

def Input_Char_FIO(): 
    char = int(input('Введите характерстику:\n1 - По ID\n2 - по ФИО\n3 - по телефону\n  Введите: '))
    return char
    
    
    


# id,ФИО,дата рождения
# 21,Максим Иванов,29.05.1999
# 1)Ввод нового пользователя
# 2)Поиск по определенной характеристике -> ввод хар-стики, предлагаем на выбор строчки подходящие, полтзователь 
# выбирает и мы изменяем