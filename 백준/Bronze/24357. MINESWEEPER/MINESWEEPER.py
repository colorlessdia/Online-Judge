graph = [list(map(int, input().split())) for _ in range(3)]

dy = [1, 1, 1, 0, -1, -1, -1, 0]
dx = [-1, 0, 1, 1, 1, 0, -1, -1]

for i in range(3):

    for j in range(3):

        if graph[i][j] == 9:
            continue

        count = 0

        for k in range(8):
            y, x = i + dy[k], j + dx[k]

            if not ((0 <= y < 3) and (0 <= x < 3)):
                continue

            if graph[y][x] == 9:
                count += 1
        
        graph[i][j] = count

for line in graph:
    print(*line)