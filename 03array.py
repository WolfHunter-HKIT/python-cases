m = [3, 4, 9, -1, 83, 8, 3, 9, 7, 3, 8]

m.append(1313)
print(m)

m.insert(1, 1001)
print(m)

print(m.count(8))
print(m.index(8))

# m.sort()
m.sort(reverse=True)
print(m)

txt = ['a', 'ab', 'bb', 'b', 'abc', 'ba']
txt.sort(key=len)
print(txt)

txt.reverse()