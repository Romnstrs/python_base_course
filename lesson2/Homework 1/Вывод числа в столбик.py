x=100
y=10
digit= input('Введите четырезначное число:')
digit= int(digit)
higher_grade, lower_grade = divmod(digit, x)
a, b = divmod(higher_grade, y)
c,d = divmod(lower_grade, y)
print(a)
print(b)
print(c)
print(d)
