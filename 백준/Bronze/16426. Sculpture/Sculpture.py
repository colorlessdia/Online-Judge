import sys

input = sys.stdin.readline

R, C = map(int, input().split())

graph = [list(map(int, input().split())) for _ in range(R)]
drain_list = [[0 for _ in range(C)] for _ in range(R)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for i in range(1, R - 1):

    for j in range(1, C - 1):
        p = graph[i][j]
        count = 0

        for k in range(4):
            y = i + dy[k]
            x = j + dx[k]
            q = graph[y][x]

            if p < q:
                count += 1
        
        if count == 4:
            drain_list[i][j] = 1

for line in drain_list:
    print(*line)