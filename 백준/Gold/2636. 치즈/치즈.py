import sys
from collections import deque

def BFS():
    queue = deque([(0, 0)])
    visited = [[False for _ in range(C)] for _ in range(R)]
    visited[0][0] = True

    dy = [1, 0, -1, 0]
    dx = [0, 1, 0, -1]

    melted_cheese_count = 0
    melted_cheese_dict = dict()

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            Y, X = y + dy[i], x + dx[i]

            if not ((0 <= Y < R) and (0 <= X < C)):
                continue

            if visited[Y][X]:
                continue

            if graph[Y][X] == 0:
                queue.append((Y, X))
                visited[Y][X] = True
                continue

            melted_cheese_dict[(Y, X)] = 1
    
    for my, mx in melted_cheese_dict:
        graph[my][mx] = 0
        melted_cheese_count += 1

    return melted_cheese_count

input = sys.stdin.readline

R, C = map(int, input().split())

graph = [[0 for _ in range(C)] for _ in range(R)]
cheese = 0

for r in range(R):
    row = list(map(int, input().split()))

    for c in range(C):
        col = row[c]
        graph[r][c] = col

        if col == 1:
            cheese += 1

time = 0
before_melted_cheese = 0

while 0 < cheese:
    melted_cheese_count = BFS()
    before_melted_cheese = melted_cheese_count

    cheese -= melted_cheese_count
    time += 1

print(time)
print(before_melted_cheese)