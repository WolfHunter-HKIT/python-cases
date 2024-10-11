import math

skaiciai = map(int,input('Iveskite skaiciu(-ius)').split(','))
operator = input('Ka su juo(jais) norite daryti. Iveski operatoriu: +, -, *, /, ^(laipsnis), q(saknis)')

match operator:
    case '+':
        print(f'Atsakymas: {sum(skaiciai)}')
    case '-':
        print(f'Atsakymas: {int(skaiciai[0]) - int(skaiciai[1])}')
    case '*':
        print(f'Atsakymas: {int(skaiciai[0]) * int(skaiciai[1])}')
    case '/':
        print(f'Atsakymas: {int(skaiciai[0]) / int(skaiciai[1])}(sveikas) \n{int(skaiciai[0]) // int(skaiciai[1])}(nesuapvalintas)')
    case '^':
        print(f'Atsakymas: {pow(skaiciai)}')
    case 'q':
        print(f'Atsakymas: {math.sqrt(skaiciai)}')
    case _:
        print(f'{operator} Neteisingas operatorius')