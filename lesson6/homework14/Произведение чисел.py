i= int(input("Введите число: "))
j=0
while i>9:
    task = tuple(str(i))
    i=1
    while j<len(task):
        i*=int(task[j])
        j+=1
    j=0
print(i)