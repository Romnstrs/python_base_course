cont='yes'
first_digit = input('Введите первое число:')
first_digit = float(first_digit)
while cont=='yes' or cont== 'y':
    sign = input('Введите желаемое простое действие:')
    second_digit = input('Введите второе число:')
    second_digit = float(second_digit)
    print(first_digit, sign, second_digit)
    if sign == '+':
        first_digit += second_digit
        print(first_digit)
    elif sign == '-':
        first_digit -= second_digit
        print(first_digit)
    elif sign == '*':
        first_digit *= second_digit
        print(first_digit)
    elif second_digit == 0 and sign == '/':
        print('На ноль делить нельзя')
    elif sign == '/':
        first_digit /= second_digit
        print(first_digit)
    else:
        print('Простые действия это "+" - сумма, "-" - разница, "*" - умножение, "/" - деление. Выберите одно из них и введите его')
    cont = input("Если хотите продолжить вычисления введите yes или y :")
    cont = cont.strip()
    cont = cont.lower()