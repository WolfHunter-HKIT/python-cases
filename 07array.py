eil = '52, 87, 98, 47, 54'
# galGeriau = list(eil.split(', '))
# sk = []
# for i in galGeriau:
#     sk.append(int(i))
# print(sk)

# sk = [int(i) for i in list(eil.split(', '))]

sar = list(range(1, 10))
kvSar = [i*i for i in sar]

print(kvSar)

lygSarKv = [i*i for i in sar if i % 2 == 0]
print(lygSarKv)