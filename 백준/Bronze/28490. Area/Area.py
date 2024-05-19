import sys

n = int(sys.stdin.readline())

max_frame = 0

for _ in range(n):
    h, w = map(int, sys.stdin.readline().split())

    if max_frame < h * w:
        max_frame = h * w

print(max_frame)