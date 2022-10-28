lst=[1,2,3,'2','g']
if len(lst)==0:
    lst.extend([[],[]])
    print(lst)
elif len(lst)==1:
    x=[[]]
    x.insert(0,lst)
    print(x)
elif len(lst)%2==0:
    x=int(len(lst)/2)
    y=[]
    y.append(lst[0:x])
    y.append(lst[x:len(lst)])
    print(y)
else:
    x = int(len(lst) / 2)+1
    y = []
    y.append(lst[0:x])
    y.append(lst[x:len(lst)])
    print(y)
