#  Įvedamas skaičius, perrašyti jį atvirkščiai.

sk = list(input('Įveskite skaičių.\n'))
length = len(sk) - 1
i = 0

while length > i:
    sk.remove(length)
    sk.insert(i, sk[len(sk)])
    i += 1

print(sk)

