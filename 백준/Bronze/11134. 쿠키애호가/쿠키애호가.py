import sys

for _ in range(int(input())):
    n, c = map(int, sys.stdin.readline().split())

    print(n // c) if n % c == 0 else print((n // c) + 1)