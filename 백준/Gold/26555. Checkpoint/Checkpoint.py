import sys
from collections import deque

def BFS(graph, move_map, start, end, R, C):
    queue = deque([start])
    move_map[start[0]][start[1]] = 1

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            Y, X = y + dy[i], x + dx[i]

            if not ((0 <= Y < R) and (0 <= X < C)):
                continue
            
            if graph[Y][X] == '#' or move_map[Y][X] != 0:
                continue
            
            move_map[Y][X] = move_map[y][x] + 1
            queue.append((Y, X))

            if (Y, X) == end:
                return move_map[Y][X] - 1

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    R, C, D = map(int, input().split())

    graph = [[0 for _ in range(C)] for _ in range(R)]
    goal_list = [0] * (D + 2)

    for i in range(R):
        row = input().rstrip()

        for j in range(C):
            col = row[j]
            graph[i][j] = col

            if col == 'S':
                goal_list[0] = (i, j)
            elif col == 'E':
                goal_list[-1] = (i, j)
            elif col.isnumeric():
                goal_list[int(col)] = (i, j)
    
    distance = 0

    for i in range(1, D + 2):
        move_map = [[0 for _ in range(C)] for _ in range(R)]

        distance += BFS(graph, move_map, goal_list[i - 1], goal_list[i], R, C)

    print(distance)