import sys
from collections import deque

def calc_coordinates(cy, cx, direction):
    matched_direction = dict(zip(list('URDL'), range(4)))
    d = matched_direction[direction]
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    return (cy + dy[d], cx + dx[d])

def BFS(graph, view_map, sy, sx):
    queue = deque([(sy, sx)])
    target = graph[sy][sx]
    view_map[sy][sx] = '.'

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            Y, X = y + dy[i], x + dx[i]

            if not ((0 <= Y < R) and (0 <= X < C)):
                continue

            if view_map[Y][X] == '.':
                continue

            if graph[Y][X] == target:
                view_map[Y][X] = '.'
                queue.append((Y, X))

input = sys.stdin.readline

R, C = map(int, input().split())

graph = [[0 for _ in range(C)] for _ in range(R)]
view_map = [['#' for _ in range(C)] for _ in range(R)]

for i in range(R):
    row = input().rstrip()
    
    for j in range(C):
        col = row[j]
        graph[i][j] = col

HR, HC = map(lambda x: int(x) - 1, input().split())
do_sequence = input().rstrip()

for do in do_sequence:

    if do != 'W':
        HR, HC = calc_coordinates(HR, HC, do)
        continue

    if view_map[HR][HC] == '#':
        BFS(graph, view_map, HR, HC)

dy = [0, -1, 0, 1, 0]
dx = [0, 0, 1, 0, -1]

for i in range(5):
    y, x = HR + dy[i], HC + dx[i]

    if not ((0 <= y < R) and (0 <= x < C)):
        continue

    if view_map[y][x] == '#':
        view_map[y][x] = '.'

for row in view_map:
    print(''.join(row))