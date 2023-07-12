def Write_Name(name):
    with open('D:/Works/IT/Python_Start/Education/GeekBrains/Python/Seminar/Tel/telephone.txt', 'a', encoding='utf-8') as file:
        file.write(name)
        
def Search_Data(data, iter1, iter2):
    with open('D:/Works/IT/Python_Start/Education/GeekBrains/Python/Seminar/Tel/telephone.txt', 'r', encoding='utf-8') as file:
        lst = file.readlines()
        res = 'Такого пользователя нет'
        for row in lst:
            temp = row.split(',')
            if data == temp[iter1][iter2]: 
                res = row
    return res
            
def Print_All():   # вывод всего списка
    with open('D:/Works/IT/Python_Start/Education/GeekBrains/Python/Seminar/Tel/telephone.txt', 'r', encoding='utf-8') as file:
        lst = list(map(lambda x: x.strip(), file.readlines()))
    return lst

def Sort_list_ID_Phone(char):   # сортировка по ID или телефону
    with open('D:/Works/IT/Python_Start/Education/GeekBrains/Python/Seminar/Tel/telephone.txt', 'r', encoding='utf-8') as file:
        lst = list(map(lambda x: x.strip(), file.readlines()))
        lst.sort(key = lambda x: int(x.split(',')[char]))
        return lst
    
def Sort_list_Name(char):   # сортировка по ФИО
    with open('D:/Works/IT/Python_Start/Education/GeekBrains/Python/Seminar/Tel/telephone.txt', 'r', encoding='utf-8') as file:
        lst = list(map(lambda x: x.strip(), file.readlines()))
        lst.sort(key = lambda x: (x.split(',')[char]))
        return lst

