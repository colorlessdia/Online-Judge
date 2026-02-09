import sys

def calc_coordinate(y, x, graph):
    dy = [0, 0, 1, 1]
    dx = [0, 1, 0, 1]

    for i in range(4):
        Y, X = y + dy[i], x + dx[i]

        if graph[Y][X] == '.':
            graph[Y][X] = '#'

input = sys.stdin.readline

N, M = map(int, input().split())

graph = [['.' for _ in range(M)] for _ in range(N)]

for i in range(N):
    row = input().rstrip()

    for j in range(M):
        col = row[j]

        if col == '.':
            continue

        calc_coordinate(i, j, graph)

for line in graph:
    print(''.join(line))