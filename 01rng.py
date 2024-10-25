import random

# paz = random.randint(1, 10)
# print(paz)

# sk = random.randrange(0, 100, 2)
# print(sk)

# tr = random.random()
# print(tr)

# txt = ['a', 'b', 'c', 'd']
# rez = random.choice(txt)
# print(rez)

txt1 = ['Ž', 'P', 'A']
for i in range(10):
    rez = random.choices(txt1, k=2)
    print(rez)