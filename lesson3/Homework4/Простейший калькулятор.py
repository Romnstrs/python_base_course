first_digit= input('Введите первое число:')
first_digit= float(first_digit)
sign= input('Введите желаемое простое действие:')
second_digit= input('Введите второе число:')
second_digit= float(second_digit)
print(first_digit,sign,second_digit)
if sign== '+':
    print(first_digit+second_digit)
elif sign== '-':
    print(first_digit-second_digit)
elif sign=='*':
    print(first_digit*second_digit)
elif second_digit== 0 and sign=='/':
    print('На ноль делить нельзя')
elif sign == '/':
    print(first_digit/second_digit)
else:
    print('Простые действия это "+" - сумма, "-" - разница, "*" - умножение, "/" - деление. Выберите одно из них и введите его' )