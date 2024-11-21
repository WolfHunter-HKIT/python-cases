x = list(range(0, 40))
neX = []

for i in x:
    if i % 2 == 0:
        neX.append(i)
        x.remove(i)
print(x, "\n", neX)