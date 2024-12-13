import sys

n = int(sys.stdin.readline())

matrix = [[] for _ in range(n)]

for i, j in enumerate(range(1, (n * n) + 1, n)):
    
    if i % 2 != 0:
        matrix[i] = list(range(j, j + n))[::-1]
    else:
        matrix[i] = list(range(j, j + n))

for row in matrix:
    print(' '.join(map(str, row)))