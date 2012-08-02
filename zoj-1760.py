import sys
from math import ceil

def main(l):
    ans = 0
    for i, num1 in enumerate(l):
        for num2 in l[i+1:]:
            if num1 * 2 == num2:
                ans = ans + 1
                break
            elif num1 * 2 < num2:
                break
    print ans

for line in sys.stdin:
    a = line.split()
    l = []
    for num in a:
        if int(num) != 0:
            l.append(int(num))
    l.sort()
    if l[0] == -1:
        break
    main(l)
