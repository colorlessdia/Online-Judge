import sys

n = int(sys.stdin.readline())

for i in range(1, n + 1):
    c = int(sys.stdin.readline())
    d = sorted(map(int, sys.stdin.readline().split()))
    t = ([0] + sorted(map(int, sys.stdin.readline().split())))[::4][1:][::-1]

    maximun_time = max([dd + tt for dd, tt in zip(d, t)])

    print(f'Trip #{i}: {maximun_time}')