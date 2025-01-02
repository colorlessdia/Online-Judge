import sys

N = int(sys.stdin.readline())

for n in range(1, N + 1):
    print(f'Case #{n}: {' '.join(sys.stdin.readline().rstrip().split()[::-1])}')