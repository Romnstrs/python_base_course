import random
lst=[]
result=[]
for i in range(random.randint(3,10)):
    lst.append(random.randint(0,100))
result.append(lst[0])
result.append(lst[2])
result.append(lst[len(lst)-2])
print(result)