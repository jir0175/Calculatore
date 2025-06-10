try:
    number1 = int(input('Введите первое число:'))
    number2 = int(input('Введите второе число:'))
    result = int(input('1.Сложение \n2.Вычитание \n3.Умножение \n4.Деление \nВыберите одно из выше перечисленных действий:'))
    if result == 1:
        print(f"Ответ:{number1 + number2}")
    elif result == 2:
        print(f"Ответ:{number1 - number2}")
    elif result == 3:
        print(f"Ответ:{number1 * number2}")
    elif result == 4:
        print(f"Ответ:{number1 / number2}")
    else:
        print('Ошибка')
except ValueError:
    print('Вы напутали что то с числами')
