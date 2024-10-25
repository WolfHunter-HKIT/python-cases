# Įvedama pradinė reikšmė p ir galutinė g.
# Atspausdinkite visus lyginius skaičius iš šio intervalo.

p, g = map(int, input('Įveskite intervalą atskirtą dvitaškiu(:).\n').split(':'))

if (p % 2 != 0):
    p = p + 1

for i in range(p, g+1, 2):
    print(i)