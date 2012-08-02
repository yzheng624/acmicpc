

import sys

for line in sys.stdin:
    line = line.split()[0]
    if line == '0':
        break
    else:
        ans = 0
        fac = 1
        for i in reversed(line):
            ans = ans + int(i) * fac
            fac = (fac + 1) * 2 - 1
        print ans