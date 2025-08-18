import sys
from heapq import heappush, heappop

input = sys.stdin.readline

problem_number = 0

while 1:
    N = int(input())

    if N == 0:
        break

    INF = float('inf')

    graph = [list(map(int, input().split())) for _ in range(N)]
    dist = [[INF for _ in range(N)] for _ in range(N)]
    dist[0][0] = graph[0][0]

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    priority_queue = [(graph[0][0], (0, 0))]

    while priority_queue:
        w1, (y, x) = heappop(priority_queue)

        if dist[y][x] < w1:
            continue

        for i in range(4):
            Y, X = y + dy[i], x + dx[i]

            if not ((0 <= Y < N) and (0 <= X < N)):
                continue

            w = w1 + graph[Y][X]

            if w < dist[Y][X]:
                dist[Y][X] = w
                heappush(priority_queue, (w, (Y, X)))

    problem_number += 1
    
    print(f'Problem {problem_number}: {dist[N - 1][N - 1]}')