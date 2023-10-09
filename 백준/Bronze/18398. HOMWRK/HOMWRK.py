import sys

t = int(input())

for _ in range(t):
    for _ in range(int(input())):
        a, b = map(int, sys.stdin.readline().rstrip().split())

        print((a + b), (a * b))