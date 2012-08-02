import sys

n = 0
l = []
t = []
for line in sys.stdin:
    a = line.split()
    if n == 0:
        n = int(a[0])
        l.append(t)
        t = []
    else:
        t.append([int(i) for i in a])
        n = n - 1
l.remove([])

for mat in l:
    x = sum([1 for j in [sum(i) for i in mat] if j % 2 != 0])
    y = sum([1 for j in [sum(i) for i in zip(*mat)] if j % 2 != 0])
    if x == 0 and y == 0:
        print 'OK'
    elif x == 1 and y == 1:
        x = [k for k, j in enumerate([sum(i) for i in mat]) if j % 2 != 0]
        y = [k for k, j in enumerate([sum(i) for i in zip(*mat)]) if j % 2 != 0]
        print 'Change bit ({},{})'.format(x[0]+1, y[0]+1)
    else:
        print 'Corrupt'