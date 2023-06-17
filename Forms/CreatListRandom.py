def Creat_list1(n):
    from random import randint
    data = []
    for i in range(0, n):
        data.append(randint(0, 20))
    print(data)
    return data

def Creat_list2(n):
    from random import randint
    data = [randint(0, 10) for i in range(n)]
    print(data)
    return data