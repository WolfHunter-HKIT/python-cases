diena = int(input('iveskite savaites diena...'))
match diena:
    case 1 | 2 | 3 | 4 | 5:
        txt = 'Darbo diena'
    case 6 | 7:
        txt = 'Savaitgalis'
    case _:
        txt = 'Blogi Duomenys'
print(f'{diena} ------> {txt}')