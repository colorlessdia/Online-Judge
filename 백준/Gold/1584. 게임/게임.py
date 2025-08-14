from collections import deque

def BFS():
    INF = float('inf')

    queue = deque([(0, 0)])
    dist = [[INF for _ in range(500 + 1)] for _ in range(500 + 1)]
    dist[0][0] = 0
    graph[0][0] = 0

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    while queue:
        y, x = queue.popleft()

        if y == x == 500:
            return dist[y][x]

        for i in range(4):
            Y, X = y + dy[i], x + dx[i]

            if not ((0 <= Y <= 500) and (0 <= X <= 500)):
                continue

            if graph[Y][X] < 0:
                continue

            value = graph[Y][X]

            if dist[y][x] + value < dist[Y][X]:
                dist[Y][X] = dist[y][x] + value

                if value == 0:
                    queue.appendleft((Y, X))
                else:
                    queue.append((Y, X))

    return -1

graph = [[0 for _ in range(500 + 1)] for _ in range(500 + 1)]

N = int(input())

for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())

    y1, y2 = min(y1, y2), max(y1, y2)
    x1, x2 = min(x1, x2), max(x1, x2)

    for y in range(y1, y2 + 1):

        for x in range(x1, x2 + 1):
            graph[y][x] = 1

M = int(input())

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())

    y1, y2 = min(y1, y2), max(y1, y2)
    x1, x2 = min(x1, x2), max(x1, x2)

    for y in range(y1, y2 + 1):

        for x in range(x1, x2 + 1):
            graph[y][x] = -1

print(BFS())