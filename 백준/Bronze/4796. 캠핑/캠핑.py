import sys

case = 1

while True:
    L, P, V = map(int, sys.stdin.readline().split())

    if L == 0 and P == 0 and V == 0:
        break

    q = V // P * L
    r = V % P

    if r <= L:
        print(f'Case {case}: {q + r}')
    else:
        print(f'Case {case}: {q + L}')

    case += 1