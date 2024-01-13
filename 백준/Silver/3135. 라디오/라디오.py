import sys

A, B = map(int, input().split())
N = int(input())

a_b_diff = abs(A - B)
count = a_b_diff

for _ in range(N):
    hz = int(sys.stdin.readline())

    if hz == B:
        count = 1
        break

    b_hz_diff = abs(B - hz)
    
    if b_hz_diff + 1 < count:
        count = b_hz_diff + 1

print(count)