import sys

t = int(sys.stdin.readline())

for _ in range(t):
    p, q = map(int, sys.stdin.readline().split())

    f = (p * q) / (p + q)

    print('f = {:.1f}'.format(f))