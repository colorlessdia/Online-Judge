import sys

for _ in range(int(input())):
    p, t = map(int, sys.stdin.readline().rstrip().split())

    d = t // 7
    b = t // 4

    print(p - d + b)