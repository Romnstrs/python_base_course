k=10000
p=1000
n=100
l=10
digit= input('Введите пятизначное число:')
digit= int(digit)
a, lower_grade = divmod(digit, k)
b, lower_grade = divmod(lower_grade, p)
c, lower_grade = divmod(lower_grade, n)
d, e = divmod(lower_grade, l)
result=e*k + d*p + c*n + b*l + a
print(result)