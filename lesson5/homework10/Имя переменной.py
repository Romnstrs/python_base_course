import keyword
import string
i=0
result='True'
tsk = input('Введите строку на проверку: ')
tsk = tsk.rstrip()
while i < len(keyword.kwlist):
    if tsk == keyword.kwlist[i]:
        result = ('False')
        break
    else:
        i += 1
for char in tsk:
    for sign in string.punctuation:
        if char == sign or char == " ":
            if char =="_":
                continue
            else:
                result=('False')
                break
    for caps in string.ascii_uppercase:
        if char == caps:
            result=('False')
            break
for numb in string.digits:
    if tsk[0] == numb:
        result=('False')
print(result)