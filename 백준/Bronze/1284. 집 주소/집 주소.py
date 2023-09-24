import sys

while 1:
    s = sys.stdin.readline().rstrip()

    if s == '0': break

    total = len(s) + 1

    for ss in s:
        if ss == '0':
            total += 4
        elif ss == '1':
            total += 2
        else:
            total += 3
    
    print(total)