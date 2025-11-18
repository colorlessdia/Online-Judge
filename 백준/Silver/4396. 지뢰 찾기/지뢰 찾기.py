import sys

def find_mine(mine_graph, y, x):
    dy = [1, 1, 1, 0, -1, -1, -1, 0]
    dx = [-1, 0, 1, 1, 1, 0, -1, -1]

    count = 0

    for i in range(8):
        Y, X = y + dy[i], x + dx[i]

        if not ((0 <= Y < N) and (0 <= X < N)):
            continue

        if mine_graph[Y][X] == '*':
            count += 1
    
    return count

input = sys.stdin.readline

N = int(input())

graph = [['.' for _ in range(N)] for _ in range(N)]
mine_graph = [input().rstrip() for _ in range(N)]
square_graph = [input().rstrip() for _ in range(N)]

mine_list = []
is_find = False

for i in range(N):

    for j in range(N):
        mine = mine_graph[i][j]
        square = square_graph[i][j]

        if mine == '*':
            mine_list.append((i, j))

            if square == 'x' and (not is_find):
                is_find = True

        if square == 'x':
            count = find_mine(mine_graph, i, j)
            graph[i][j] = str(count)

if is_find:

    for y, x in mine_list:
        graph[y][x] = '*'

for line in graph:
    print(''.join(line))