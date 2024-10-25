# Įvedami 2 skaičiai sk1 ir sk2.
# Parašyti programą, kuri randa didžiausią bendra daliklį.

sk1, sk2 = map(int, input('Įrašykite 2 skaičius atskirtus tarpu.\n').split(' '))
higher = sk1

if (sk1 < sk2):
    higher = sk2

for i in range(higher, 0, -1):
    if (sk1 % i == 0 and sk2 % i == 0):
        print(f'Didžiausias bendras daliklis yra {i}')
        break
