import sys
from math import ceil

def main(n,u,d):
    t = int(ceil(((n-u)/(u-d)))*2.0 + 1.0)
    print t

for line in sys.stdin:
    a = line.split()
    n, u, d = float(a[0]), float(a[1]), float(a[2])
    if n == 0.0:
        break
    main(n,u,d)
