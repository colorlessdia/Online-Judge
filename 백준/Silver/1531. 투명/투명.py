import sys

coordinate_map = [[0 for _ in range(100 + 1)] for _ in range(100 + 1)]

mosaic_count = dict()

N, M = map(int, sys.stdin.readline().split())

for _ in range(N):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for x in range(x1, x2 + 1):
        
        for y in range(y1, y2 + 1):
            coordinate_map[x][y] += 1

            if coordinate_map[x][y] <= M:
                continue
            
            if (x, y) in mosaic_count:
                continue
            
            mosaic_count[(x, y)] = 1

print(len(mosaic_count))