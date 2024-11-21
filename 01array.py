m = [3, 4, 9, -1, 83, 8]

print(type(m))
print(m)

user = ["Jonas", 18, 1.78, True, [8, 9, 4, 8]]
print(user[-1])
print(user[-1][0])

for i in m:
    i = i + 1
    print(i)
print(m)

for i in range(len(m)):
    m[i] += 1
print(m)
print(m*2)

m = user + m
print(m)

print(len(user[-1]))

eil = '52, 87, 98, 47, 54'
galSk = list(eil)
print(galSk)

galGeriau = list(eil.split(', '))
print(galGeriau)