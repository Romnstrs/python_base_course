lst=[6]
i=0
x=0
while i<len(lst):
    if i%2==0:
        x+=lst[i]
        i+=1
    else:
        i+=1
if len(lst)>0:
    x=x*lst[len(lst)-1]
else:
    x=0
print(x)