import sys
t = int(input())
for i in range(1, t + 1):
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().rstrip()

    for ss in s:
        if ss == 'b':
            n -= 1
        elif ss == 'c':
            n += 1
    
    print(f'Data Set {i}:')
    print(n)
    if i != t:
        print('')