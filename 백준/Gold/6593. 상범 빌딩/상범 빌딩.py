import sys
from collections import deque

def BFS(graph, start_point, end_point, L, R, C):
    queue = deque([start_point[0]])

    dz = [0, 0, 0, 0, 1, -1]
    dy = [1, 0, -1, 0, 0, 0]
    dx = [0, 1, 0, -1, 0, 0]

    while queue:
        z, y, x, time = queue.popleft()

        if (z, y, x) == end_point:
            return time

        for i in range(6):
            c, b, a = z + dz[i], y + dy[i], x + dx[i]

            if not ((0 <= c < L) and (0 <= b < R) and (0 <= a < C)):
                continue
            
            if graph[c][b][a] == 0:
                graph[c][b][a] = time + 1
                queue.append((c, b, a, time + 1))

input = sys.stdin.readline

while 1:
    L, R, C = map(int, input().split())

    if L == R == C == 0:
        break
    
    building = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]
    start_point = []
    end_point = []
    
    for l in range(L):

        for r in range(R + 1):
            row = input().rstrip()

            if r == R:
                continue
            
            for c in range(C):
                col = row[c]

                if col == '#':
                    building[l][r][c] = -1
                    continue
                
                if col == 'S':
                    start_point.append((l, r, c, 0))
                    continue
                
                if col == 'E':
                    end_point.append((l, r, c))
                    continue

    BFS(building, start_point, end_point, L, R, C)

    el, er, ec = end_point[0]
    minute = building[el][er][ec]

    if minute:
        print(f'Escaped in {minute} minute(s).')
    else:
        print('Trapped!')