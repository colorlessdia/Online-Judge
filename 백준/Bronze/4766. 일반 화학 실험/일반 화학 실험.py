import sys

before = 999

while 1:
    n = float(sys.stdin.readline())

    if n == 999: break

    if before != 999:
        print(f'{(n - before):.2f}')

    before = n