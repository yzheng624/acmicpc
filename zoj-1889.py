import sys

for line in sys.stdin:
    num = int(line)
    k = 1
    while k % num != 0:
        k = k * 10 + 1
    print len(str(k))