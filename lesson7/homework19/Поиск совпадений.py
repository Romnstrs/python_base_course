import random
lst3=[]
lst5=[]
for i in range(random.randint(0,100)):
    lst3.append((i+1)*3)
for i in range(random.randint(0,100)):
    lst5.append((i+1)*5)
result=set(lst3).intersection(set(lst5))
print(result)