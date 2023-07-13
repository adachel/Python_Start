from view import *
def Write_Name(name):
    with open('D:/Works/IT/Python_Start/Education/GeekBrains/Python\HomeWork/Tel/telephone.txt', 'a', encoding='utf-8') as file:
        file.write(name)
        
def Search_Data(data, *args): # поиск
    with open('D:/Works/IT/Python_Start/Education/GeekBrains/Python\HomeWork/Tel/telephone.txt', 'r', encoding='utf-8') as file:
        lst = file.readlines()
        res = 'Такого пользователя нет'
        res_temp = ''
        for row in lst:
            row_temp = row.split(',')
            temp = row_temp[args[0]].split()
            if data == temp[args[1]]: 
                res_temp = res_temp + row
        if res_temp is not '':
            res = res_temp
    return res
            
def Print_All():   # вывод всего списка
    with open('D:/Works/IT/Python_Start/Education/GeekBrains/Python\HomeWork/Tel/telephone.txt', 'r', encoding='utf-8') as file:
        lst = list(map(lambda x: x.strip(), file.readlines()))
    return lst

def Sort_list_ID_Phone(char):   # сортировка по ID или телефону
    with open('D:/Works/IT/Python_Start/Education/GeekBrains/Python\HomeWork/Tel/telephone.txt', 'r', encoding='utf-8') as file:
        lst = list(map(lambda x: x.strip(), file.readlines()))
        lst.sort(key = lambda x: int(x.split(',')[char]))
        return lst
    
def Sort_list_Name(char):   # сортировка по ФИО
    with open('D:/Works/IT/Python_Start/Education/GeekBrains/Python\HomeWork/Tel/telephone.txt', 'r', encoding='utf-8') as file:
        lst = list(map(lambda x: x.strip(), file.readlines()))
        lst.sort(key = lambda x: (x.split(',')[char]))
        return lst

def Remove(data):   # Удаление
    with open('D:/Works/IT/Python_Start/Education/GeekBrains/Python\HomeWork/Tel/telephone.txt', 'r', encoding='utf-8') as file:
        lst = list(map(lambda x: x.strip(), file.readlines()))
        data = list(data.split('\n'))
        for row in data:
            if row in lst:
                lst.remove(row)
    with open('D:/Works/IT/Python_Start/Education/GeekBrains/Python\HomeWork/Tel/telephone.txt', 'w', encoding='utf-8') as file:
        for row in lst:
            file.write(row + '\n')
    return lst

def Rename(data):
    with open('D:/Works/IT/Python_Start/Education/GeekBrains/Python\HomeWork/Tel/telephone.txt', 'r', encoding='utf-8') as file:
        lst = list(map(lambda x: x.strip(), file.readlines()))
        data = list(data.split('\n'))
        for row in data:
            if row in lst:
                print(f'Текущие данные {row}\nИзменить? (y или n) ')
                temp = input()
                if temp == 'y':
                    lst.remove(row)
                    row = Input_Name1()
                    lst.append(row)
                elif input() == 'n': break
    with open('D:/Works/IT/Python_Start/Education/GeekBrains/Python\HomeWork/Tel/telephone.txt', 'w', encoding='utf-8') as file:
        for row in lst:
            file.write(row + '\n')
    return lst
                
                    

