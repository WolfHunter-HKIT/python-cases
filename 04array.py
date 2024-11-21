m = [3, 4, 9, -1, 83, 8, 3, 9, 7, 3, 8]
kitas = [1, 1, 1, 1]


ka = m.pop(1)

print(m, ka)

ka = m.remove(8)
print(m, ka)

m.extend(kitas)
print(m)

kitas.clear()
print(kitas)

print(max(m))
print(sum(m))
print(min(m))

del m[5]
print(m)