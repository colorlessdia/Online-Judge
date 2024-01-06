import sys
n = int(sys.stdin.readline().strip())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if (i == j):
            print('*' * j, end=' ')
    print()