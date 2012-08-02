import sys

for i, line in enumerate(sys.stdin):
    if i == 0:
        continue
    a = line.split()
    n = float(a[0])
    total = sum([float(s) for s in a[1:]])
    avg = total / n
    above = sum([1 for stu in a[1:] if float(stu) > avg])
    print '{0:.3f}%'.format(above / n * 100)
