def add_one(lst: list):
    j = -1
    if lst[0]>=0 or len(lst)==1:
        lst[-1] += 1
    elif lst[-1]==0 and len(lst)==2:
        lst[-2]+=1
        lst[-1]=9
        if lst[0]==0:
            del(lst[0])
            lst[-1]=-9
    else:
        lst[-1]-=1
        i=-1
        k = lst[0]
        while i>-len(lst):
            if lst[i]<0:
                lst[i-1]-=1
                lst[i]=9
            i-=1
        if k > lst[0]:
            del(lst[0])
            lst[0]*=-1
    while j > -len(lst):
        if lst[j] == 10:
            lst[j - 1] += 1
            lst[j] = 0
        j -= 1
    if lst[0] == 10:
        lst.append(0)
        lst[0] = 1
    return lst


lst=list(input("Type some number: "))
i=0
if lst[0]=='-':
    del(lst[0])
    lst[0]='-'+lst[0]
while i<len(lst):
    lst[i]=int(lst[i])
    i+=1
print(add_one(lst))