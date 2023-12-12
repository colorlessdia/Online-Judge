import sys

for i in range(1, int(input()) + 1):
    a, b, x = map(int, sys.stdin.readline().split())

    print(a * (x - 1) + b)