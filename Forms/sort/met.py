# a = ["10,Иван,15","3,Алеша,10",]
# a.sort(key = lambda x: int(x.split(",")[2]))
#print(a)
a = [(6,5),(8,2),(3,7),(1,4),]
print(max(a,key=lambda x: x[1]))
print(a)