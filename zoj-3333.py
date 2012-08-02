import sys
from math import floor
import datetime

def solve(javaman, cpcs):
    if javaman < cpcs:
        print 'javaman'
    elif javaman > cpcs:
        print 'cpcs'
    else:
        print 'same'

for i, line in enumerate(sys.stdin):
    if i == 0:
        continue
    d = line.split()
    javaman = datetime.date(int(d[0]), int(d[1]), int(d[2]))
    cpcs = datetime.date(int(d[3]), int(d[4]), int(d[5]))
    solve(javaman, cpcs)
