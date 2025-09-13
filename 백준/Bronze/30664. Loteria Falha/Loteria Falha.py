import sys

input = sys.stdin.readline

while 1:
    N = int(input())

    if N == 0:
        break

    if N % 42 == 0:
        print('PREMIADO')
    else:
        print('TENTE NOVAMENTE')