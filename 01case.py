diena = input('iveskite savaites diena...')
match diena:
    case '1':
        txt = 'Pirmadienis'
    case '2':
        txt = 'Antradienis'
    case '3':
        txt = 'Treciadienis'
    case '4':
        txt = 'Ketvirtadiens'
    case '5':
        txt = 'Penktadienis'
    case '6':
        txt = 'Sestadienis'
    case '7':
        txt = 'Sekmadienis'
    case _:
        txt = 'Blogi Duomenys'
print(f'{diena} ------> {txt}')