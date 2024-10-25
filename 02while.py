# Mandagi programa sako labas ir klausia ar nori dar pasisveikitni

pasirinkimas = True

while pasirinkimas:
    print('Labas')
    ans = input('Ar norite dar sveikitnis?(T/N)\n')
    if ans != 'T' and ans != 't':
        pasirinkimas = False
print('Viso gero')
        