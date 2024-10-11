# Petriukas gavo 3 pazymius.
# Parasyti programa, kuri apskaiciutu vidurki.
# Jei ivedamas neteisingas pazymys - kartoti ivedima
# Nenaudoti For ir While
#or or :
klaidos = [0, 0, 0]

def programa():
    sk1, sk2, sk3 = map(int, input('sk1, sk2, sk3 = ').split(', '))
    
    if 0<sk1<11 and 0<sk2<11 and 0<sk3<11:
        suma = sk1 + sk2 + sk3
        vid = suma / 3
        return print(vid)
    else:
        if not(0<sk1<11):
            klaidos[0] = klaidos[0] + 1
        elif not(0<sk2<11):
            klaidos[1] = klaidos[1] + 1
        elif not(0<sk3<11):
            klaidos[2] = klaidos[2] + 1
        print(f'Neteisingas {sk1, sk2, sk3} ivesti {klaidos} kartu.')
        return programa()
    
    
        


programa()


