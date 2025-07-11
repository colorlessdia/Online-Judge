import sys
from heapq import heappush, heappop

input = sys.stdin.readline

N, M = map(int, input().split())

visited = set()
priority_corn = []
graph = [[0 for _ in range(M)] for _ in range(N)]

for i in range(N):
    row = list(map(int, input().split()))

    for j in range(M):
        col = row[j]
        graph[i][j] = col

        if (i == 0) or (i == N - 1) or (j == 0) or (j == M - 1):
            heappush(priority_corn, (-col, (i, j)))
            visited.add((i, j))

K = int(input())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for _ in range(K):
    corn, (y, x) = heappop(priority_corn)
    corn = -corn

    print(y + 1, x + 1)

    for i in range(4):
        Y, X = y + dy[i], x + dx[i]

        if not ((0 <= Y < N) and (0 <= X < M)):
            continue

        if (Y, X) in visited:
            continue

        heappush(priority_corn, (-graph[Y][X], (Y, X)))
        visited.add((Y, X))