import sys

while True:
    try:
        N, B, M = map(float, sys.stdin.readline().split())

        year = 0

        while N < M:
            year += 1

            N += N * (B / 100)

        print(year)
    except:
        break