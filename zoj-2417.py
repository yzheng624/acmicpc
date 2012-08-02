import sys

for line in sys.stdin:
    num = int(line)
    if num == 0:
        break
    k = 1
    while num & k == 0:
        k = k << 1
    print num & k