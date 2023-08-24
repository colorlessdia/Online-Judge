import sys

for _ in range(int(input())):
    n = int(sys.stdin.readline())

    print(sum([i for i in range(1, n + 1) if i % 2 != 0]))