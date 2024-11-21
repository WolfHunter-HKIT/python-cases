# Sugeneruokime sąrašą atsitiktinių ūgių nuo 166 iki 223, 20 elementų
import random

ugiai = [random.randint(166, 223) for i in range(20)]

print(ugiai)

# Sąrašą ugiai pakeisti į txt sąrašą, jei ūgis daugiau už 180 - rašyti 'aukštas', kitais atvejais - 'žemas'
ugiaiTxt = ['Aukštas' if i  >= 180 else 'Žemas' for i in ugiai]
print(ugiaiTxt)

# Sąrašą ugiai pakeisti į txt sąrašą, jei ūgis daugiau už 190 - rašyti 'aukš.', 180<ugis<190 - vid. kitais atvejais - 'žem'
ugiaiTxt = ['Aukštas' if i  >= 190 else 'Vid.' if i >= 180 else 'Žemas' for i in ugiai]
print(ugiaiTxt)


