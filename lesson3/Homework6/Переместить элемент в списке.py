lst=[1,2,]
if len(lst)==0:
    print(lst)
else:
    taker=lst.pop()
    lst.insert(0,taker)
    print(lst)