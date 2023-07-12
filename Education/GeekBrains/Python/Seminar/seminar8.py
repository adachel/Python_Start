#w - запись
#r - чтение
#a - добавить
# a = ["q\n","r\n","e\n"]
# with open("input.txt","w") as file:
#     file.write("strq\n")
#     file.writelines(a)
#with open("input.txt","r") as file:
    # print(file.read())
    # file.seek(0)
    # print(file.readlines())
    # for i in range(4):
    #     print(file.readline(i))#
    #a = list(map(lambda x: x.strip(),file.readlines()))
# with open("input.txt","a") as file:
#     file.write("qw")
    
    
a = ["10,Иван,15", "3,Алеша,10", '4,Сережа,8']
a.sort(key = lambda x: (x.split(",")[1]))
print(a)
# a = [(6,5),(8,2),(3,7),(1,4),]
# print(max(a,key=lambda x: x[1]))
# print(a)