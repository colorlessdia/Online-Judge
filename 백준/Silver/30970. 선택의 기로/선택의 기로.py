import sys

N = int(sys.stdin.readline())

M = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

Q = sorted(M, key=lambda x: (-x[0], x[1]))[:2]
P = sorted(M, key=lambda x: (x[1], -x[0]))[:2]

print(' '.join([' '.join(list(map(str, q))) for q in Q]))
print(' '.join([' '.join(list(map(str, p))) for p in P]))