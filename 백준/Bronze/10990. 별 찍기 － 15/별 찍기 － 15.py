import sys

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    
    print(' ' * (N - i), end='')

    if i == 1:
        print('*')
    else:
        print('*' + (' ' * (((i - 1) * 2) - 1))  + '*')