from database import *
from view import *

def main():
    while True:
        num = Input_Num()
        if num == 1:              
            print()
            res = Input_Name()
            Write_Name(res)
            print("Успешно записано\n")
            print()
        if num == 2:               
            print()
            char = Input_Char()
            if char == 1:
                print()
                ID = Input_ID()
                res_search = Search_Data(ID, 0, 0)
            if char == 2:
                print()
                lastName = Input_LastName()
                res_search = Search_Data(lastName, 1, 0)
            if char == 3:
                print()
                firstName = Input_FirstName()
                res_search = Search_Data(firstName, 1)     
            if char == 4:
                print() 
                phone = Input_Phone()
                res_search = Search_Data(phone, 2)    
            print()    
            print(res_search)
            print()
        if num == 3:                # сортировка
            print()
            char = Input_Sort()
            if char == 1:
                print()
                res_sort = Sort_list_ID_Phone(0)
            if char == 2:
                print()
                res_sort = Sort_list_Name(1)
            if char == 3:
                print() 
                res_sort = Sort_list_ID_Phone(2)
            for i in res_sort:    
                print(i)
            print()
        if num == 5:               
            print()
            res = Print_All()
            for i in res:
                print(i)
            print()
        if num == 6:
            break
            

main()