import sys
from math import floor

def solve(n):
    l = [1 for i in range(0, n+1)]
    for k in range(2, n+1):
        for t in range(k, n+1, k):
            if l[t] == 1:
                l[t] = 0
            else:
                l[t] = 1
    print sum(l) - 1


for i, line in enumerate(sys.stdin):
    if i == 0:
        continue
    a = line.split()
    n = int(a[0])
    solve(n)
