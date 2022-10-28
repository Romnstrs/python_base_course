import string
i=0
j=0
request=input("Введите две латинские буквы через дефиз: ")
letters=tuple(string.ascii_letters)
abetka={}
for key in string.ascii_letters:
    abetka[key] = j
    j+=1
while i < len(string.ascii_letters):
    if request[0] == string.ascii_letters[i]:
        first_key=string.ascii_letters[i]
    if request[2] == string.ascii_letters[i]:
        second_key=string.ascii_letters[i]
    i+=1
a=abetka[first_key]
b=abetka[second_key]
print(string.ascii_letters[a:b+1])