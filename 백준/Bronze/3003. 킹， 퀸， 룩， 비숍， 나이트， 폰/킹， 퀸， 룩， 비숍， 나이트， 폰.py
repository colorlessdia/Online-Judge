import sys

full_piece = [1, 1, 2, 2, 2, 8]
find_piece = list(map(int, sys.stdin.readline().split()))
need_piece = []

for i in range(len(full_piece)):
    need_piece.append(full_piece[i] - find_piece[i])

for j in need_piece:
    print(j, end=' ')