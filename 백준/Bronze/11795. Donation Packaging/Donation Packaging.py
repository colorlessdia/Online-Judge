import sys

input = sys.stdin.readline

T = int(input())

A, B, C = 0, 0, 0

for _ in range(T):
    a, b, c = map(int, input().split())

    A += a
    B += b
    C += c

    minimum_count = min(A, B, C)

    if minimum_count < 30:
        print('NO')
        continue

    A -= minimum_count
    B -= minimum_count
    C -= minimum_count
    
    print(minimum_count)