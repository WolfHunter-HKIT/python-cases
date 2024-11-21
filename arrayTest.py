import random

# 8.1
array1 = [random.randint(-50, 80) for i in range(40)]
negLen = [x for x in array1 if x < 0 and x % 2 != 0]
print(array1, '\n', len(negLen))

# 8.2
n  = random.randint(0, 12)                              # Kiek yra skirtingų prekių tipų.
A = [random.randint(20, 100) for i in range(n)]         # Kiek yrą to tipo prekių
B = []                                                  # Kiek to tipo prekių nupirkta
left = []                                               # Kiek to tipo prekių pritrūko

for x in A:
    e = random.randint(0, 100)
    if e > x:
        left.append((x - e)* -1)
        e = x
        B.append(e)
    else:
        left.append(0)
        B.append(e)
    
print(f'Yra prekių: {A}\nNupirkta prekių: {B}\nPritrūko prekių: {left}')