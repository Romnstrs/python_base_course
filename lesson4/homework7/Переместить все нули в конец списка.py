lst=[0,1,0,2,0,'0',0,3,0,[0],0,4,0]
zero_lst=[]
i=0
while i<len(lst):
    if lst[i]==0:
        del(lst[i])
        zero_lst.append(0)
    else:
        i+=1
lst+=zero_lst
print(lst)
