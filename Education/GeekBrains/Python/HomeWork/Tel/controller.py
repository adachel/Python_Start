from database import *
from view import *

def main():
    while True:
        num = Input_Num()
        
        if num == 1:      # Запись        
            res = Input_Name()
            Write_Name(res)
            print("Успешно записано\n")
            print()
            
        if num == 2:      # Поиск   
            char = Input_Char()
            if char == 1:  # по ID
                ID = Input_ID()
                res_search = Search_Data(ID, 0, 0)
            if char == 2:   # по фамилии
                lastName = Input_LastName()
                res_search = Search_Data(lastName, 1, 0)
            if char == 3:   # поимени
                firstName = Input_FirstName()
                res_search = Search_Data(firstName, 1, 1)  
            if char == 4:   # по телефону
                phone = Input_Phone()
                res_search = Search_Data(phone, 2, 0)        
            print()
            print(res_search)
            print()
        
        if num == 3:                # сортировка
            char = Input_Char_FIO()
            if char == 1:
                res_sort = Sort_list_ID_Phone(0)
            if char == 2:
                res_sort = Sort_list_Name(1)
            if char == 3:
                res_sort = Sort_list_ID_Phone(2)
            print()
            for i in res_sort:    
                print(i)
            print()
                
        if num == 4:    # Удаление
            char = Input_Char()
            if char == 1:  # по ID
                ID = Input_ID()
                res_search = Search_Data(ID, 0, 0)
                res_new = Remove(res_search)
            if char == 2:   # по фамилии
                lastName = Input_LastName()
                res_search = Search_Data(lastName, 1, 0)
                res_new = Remove(res_search)
            if char == 3:   # поимени
                firstName = Input_FirstName()
                res_search = Search_Data(firstName, 1, 1)  
                res_new = Remove(res_search)
            if char == 4:   # по телефону
                phone = Input_Phone()
                res_search = Search_Data(phone, 2, 0)  
                res_new = Remove(res_search)   
            print()       
            print(res_new)
            print()
            
        if num == 5:    # переименование
            char = Input_Char()
            if char == 1:  # по ID
                ID = Input_ID()
                res_search = Search_Data(ID, 0, 0)
                res_new = Rename(res_search)
            if char == 2:   # по фамилии
                lastName = Input_LastName()
                res_search = Search_Data(lastName, 1, 0)
                res_new = Rename(res_search)
            if char == 3:   # поимени
                firstName = Input_FirstName()
                res_search = Search_Data(firstName, 1, 1)  
                res_new = Rename(res_search)
            if char == 4:   # по телефону
                phone = Input_Phone()
                res_search = Search_Data(phone, 2, 0)  
                res_new = Rename(res_search)   
            print(res_new)
        if num == 6:    # Вывод всего списка           
            res = Print_All()
            for i in res:
                print(i)
            print()
                
        if num == 7:    # Выход из программы
            break
            

main()