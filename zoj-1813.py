import sys

for i, line in enumerate(sys.stdin):
    a = line.split()
    diameter = float(a[0]) / (12 * 5280)
    revolutions = int(a[1])
    time = float(a[2]) / 3600
    if revolutions == 0:
        break
    distance = diameter * 3.1415927 * revolutions
    mph = distance / time
    print 'Trip #{0}: {1:.2f} {2:.2f}'.format(i+1, distance, mph)
