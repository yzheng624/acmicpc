import sys

ans = []

def solve(n):
    global x, y, ans 
    if n >= minn and n <= y and n >= x:
        if n not in ans:
            ans.append(n)
            if n % 2 == 0:
                solve(n / 2)
            if n % 5 == 0:
                solve(n / 5)
    elif n >= y:
        if n % 2 == 0:
            solve(n / 2)
        if n % 5 == 0:
            solve(n / 5)
    else:
        return

for line in sys.stdin:
    a = line.split()
    x = long(a[0])
    y = long(a[1])
    ans = []
    for i in range(len(str(x)) - 1, len(str(y)) + 1):
        z = long('1' + '0' * (i))
        minn = long('1' + '0' * (i - 1))
        solve(z)
    print len(ans)