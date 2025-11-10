import sys

def calc_mine_count(graph, r, c, y, x):
    dy = [1, 1, 1, 0, -1, -1, -1, 0]
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]

    count = 0

    for i in range(8):
        Y = y + dy[i]
        X = x + dx[i]

        if not ((0 <= Y < r) and (0 <= X < c)):
            continue

        if graph[Y][X] == '*':
            count += 1

    return count

input = sys.stdin.readline

while True:
    R, C = map(int, input().split())

    if R == C == 0:
        break

    graph = [input().rstrip() for _ in range(R)]
    mine_map = [['*' for _ in range(C)] for _ in range(R)]

    for i in range(R):

        for j in range(C):
            square = graph[i][j]
            
            if square == '*':
                continue

            count = calc_mine_count(graph, R, C, i, j)
            mine_map[i][j] = str(count)
    
    for line in mine_map:
        print(''.join(line))