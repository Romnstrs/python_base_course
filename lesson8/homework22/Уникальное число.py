def find_unique_value(lst):
    k = 0
    p = 0
    n = 0
    result = list(set(lst))
    while p < len(lst):
        while k < len(lst):
            #        print("char:"+str(lst[p]))
            #        print('lst[k]:'+str(lst[k]))
            #        print(result)
            if lst[p] == lst[k]:
                if p == k:
                    k += 1
                    continue
                else:
                    while n < len(result):
                        if result[n] == lst[k]:
                            del (result[n])
                        n += 1
                    n = 0
                    break
            k += 1
        k = 0
        p += 1
    res=''
    for char in result:
        res+=str(char)+','
    return res[:len(res)-1]


lst=list(input("Type some number to create list from it: "))
i=0
j=0
while j<len(lst):
    if lst[j]=='-':
        lst[j+1]='-'+lst[j+1]
        del (lst[j])
    j+=1
while i<len(lst):
    lst[i]=int(lst[i])
    i+=1
#Можно вводить и отрицательные, но не дробные. Наример: -3212-32-1. Это разобъёт на цифры
print(find_unique_value(lst))