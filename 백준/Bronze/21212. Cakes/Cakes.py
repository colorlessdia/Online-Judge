import sys

input = sys.stdin.readline

N = int(input())

count = 10001

for _ in range(N):
    A, B = map(int, input().split())

    if B // A < count:
        count = B // A

print(count)