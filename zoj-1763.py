import sys

for i, line in enumerate(sys.stdin):
    a = line.split()
    if i == 0:
        num2 = float(a[0])
        continue
    num1, num2 = num2, float(a[0])
    if num2 == 999:
        break
    print '{0:.2f}'.format(num2 - num1)
print 'End of Output'
    
